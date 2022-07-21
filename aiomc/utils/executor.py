import os
import re
import sys
import json
import asyncio
import subprocess
import functools
import anyio
import sniffio
from typing import Union, Coroutine

PATTERN = re.compile('{(.+?)}')


class aiomcError(Exception):
    pass



def decoder(s: Union[bytes, str]):
    return s.decode('utf-8')

def stripnl(s: Union[bytes, str], source='\n'):
    return s.strip(source)

def replacenl(s: Union[bytes, str], source='\n', target=','):
    return s.replace(source, target)

def closing_curls(s: Union[bytes, str]):
    return s.replace(',}', '}')

def opening_curls(s: Union[bytes, str]):
    return s.replace('{,', '{')

def dedup_commas(s: Union[bytes, str]):
    return s.replace(',,', ',')

processors = [decoder, stripnl, replacenl, opening_curls, closing_curls, dedup_commas]


def process_string(s, processors=processors):
    for processor in processors:
        s = processor(s)
    return s

def kwarg_to_flag(**kwargs):
    _flags = []
    for _key, _value in kwargs.items():
        key = '--' + _key.replace('_', '-')
        if _value in (True, False):
            _flags.append(key)
        else:
            _flags.append(f'{key} {_value}')
    return ' '.join(_flags)


def flag_to_kwarg(flag: str):
    _flag, *_value = flag.split()
    flag_name = _flag.replace('--', '').replace('-', '_')
    value = _value.pop() if _value else True
    return {flag_name: value}


def make_json(subprocess_output, wrap=True, pair=('[', ']'), processors=processors):
    preprocessed = process_string(subprocess_output, processors=processors)
    try:
        content = json.loads(preprocessed)
    except json.JSONDecodeError as e:
        opening, closing = pair
        sequence_to_load = f'{opening}{preprocessed}{closing}'
    else:
        sequence_to_load = preprocessed
    return sequence_to_load


def get_params(cmd_template: str, pattern=PATTERN):
    params = pattern.findall(cmd_template)
    return dict(zip(params, [None] * len(params)))


def make_command_string(cmd_template: str, **kwargs):
    cmd_params = get_params(cmd_template)
    _flags = {key: value for key, value in kwargs.items() if key not in cmd_params}
    flags = kwarg_to_flag(**_flags)
    kwargs.setdefault('flags', flags)
    return cmd_template.format(**kwargs)


def execute_command(command: 'Command', wrapper_cls=None):
    wrapper_cls = wrapper_cls or Response
    arguments_list = command.command_string.split()
    try:
        _output = subprocess.check_output(arguments_list)
    except subprocess.CalledProcessError as e:
        output = e.output
    else:
        output = _output
    return wrapper_cls(
        command=command.command_string,
        name=command.name,
        output=output,
    )


async def async_execute_command(command: 'AsyncCommand', wrapper_cls = None):
    wrapper_cls = wrapper_cls or Response
    process = await asyncio.subprocess.create_subprocess_shell(command.command_string, stdout = asyncio.subprocess.PIPE, stderr = asyncio.subprocess.PIPE)
    try:
        stdout, stderr = await process.communicate()
        output = stdout.decode('UTF-8').strip()
    except (BrokenPipeError, ConnectionResetError) as e:
        output = e
    return wrapper_cls(
        command = command.command_string,
        name = command.name,
        output = output,
    )

def get_async_lib():
    try:
       return sniffio.current_async_library()
    except sniffio.AsyncLibraryNotFoundError:
       return None

def run_sync(func: Coroutine, *args, **kwargs):
    current_async_module = get_async_lib()
    partial_f = functools.partial(func, *args, **kwargs)
    if current_async_module is None:
        return anyio.run(partial_f)
    return anyio.from_thread.run(partial_f)

class Response(object):
    '''Response object for mc command line interface output.'''

    def __init__(self, command=None, name=None, output=None):
        self.command = command
        self.name = name
        self.output = output
        self.json = make_json(self.output)
        self.content = json.loads(self.json)
        try:
            self.status = self.content.get('status', 'success')
        except AttributeError:
            self.status = 'success'


    def __repr__(self):
        return f"{self.__class__.__name__}[name='{self.name}', status='{self.status}']"


class Command(object):
    def __init__(self, cmd_template = None, name = None, action = None, flags = None, docstrings = None):
        '''Command base class for MinIO mc.'''
        if flags is None:
            flags = {'json': True}
        self.name = name or self.__class__.__name__
        self.cmd_template = cmd_template
        self.action = action or execute_command
        self.flags = flags
        self.__doc__ = docstrings

    def __call__(self, **kwargs):
        if self.flags:
            kwargs.update(self.flags)
        self.command_string = make_command_string(self.cmd_template, **kwargs)
        self.result = self.action(self)
        return self.result


class AsyncCommand(object):
    def __init__(self, cmd_template = None, name = None, action = None, flags = None, docstrings = None):
        '''Command base class for MinIO mc.'''
        if flags is None: flags = {'json': True}
        self.name = name or self.__class__.__name__
        self.cmd_template = cmd_template
        self.action = action or async_execute_command
        self.flags = flags
        self.__doc__ = docstrings

    async def run(self, **kwargs):
        if self.flags: kwargs.update(self.flags)
        self.command_string = make_command_string(self.cmd_template, **kwargs)
        self.result = await self.action(self)
        return self.result

    def __call__(self, **kwargs):
        return run_sync(self.run, **kwargs)


def check_error(response: Response):
    """Checks response status and raises a 'BMCError' exception with the error message.
    """
    if response.status == 'error':
        message = response.content.get('error', {}).get('message', '')
        cause = response.content.get('error', {}).get('cause', {}).get('message', '')
        raise aiomcError(f'{message}:{cause}')


## Check for mc


def get_variable_separator():
    """
    Returns the environment variable separator for the current platform.
    :return: Environment variable separator
    """
    return ';' if sys.platform.startswith('win') else ':'

def get_binary_path(executable: str = 'mc'):
    """
    Searches for a binary named `executable` in the current PATH. If an executable is found, its absolute path is returned
    else None.
    :param executable: Name of the binary
    :return: Absolute path or None
    """
    if 'PATH' not in os.environ: return None
    for directory in os.environ['PATH'].split(get_variable_separator()):
        binary = os.path.abspath(os.path.join(directory, executable))
        if os.path.isfile(binary) and os.access(binary, os.X_OK): return binary
    return None

mc_binary_path = get_binary_path('mc')