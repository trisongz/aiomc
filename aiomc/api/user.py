'''Manage users. Command to add, remove, enable, disable, list users on MinIO server.'''

from aiomc.utils import *

__all__ = [

    'admin_user_list',
    'admin_user_add',
    'admin_user_remove',
    'admin_user_enable',
    'admin_user_disable',
    'admin_user_info',
    # Async
    'async_admin_user_list',
    'async_admin_user_add',
    'async_admin_user_remove',
    'async_admin_user_enable',
    'async_admin_user_disable',
    'async_admin_user_info',

    # Service account
    'admin_user_svcacct_add',
    'admin_user_svcacct_remove',
    'admin_user_svcacct_list',
    'admin_user_svcacct_enable',
    'admin_user_svcacct_disable',
    'admin_user_svcacct_edit',
    
    # Async
    'async_admin_user_svcacct_add',
    'async_admin_user_svcacct_remove',
    'async_admin_user_svcacct_list',
    'async_admin_user_svcacct_enable',
    'async_admin_user_svcacct_disable',
    'async_admin_user_svcacct_edit',
]


def admin_user_add(**kwargs) -> Response:
    '''Add a new user on MinIO.

    Usage::

      >>> r = admin_user_add(target='aliasforhost', username='rockstar', password='verysecretpassword')
      >>> r.content
      [{'status': 'success',
        'accessKey': 'rockstar',
        'secretKey': 'verysecretpassword',
        'userStatus': 'enabled'}]
    '''
    cmd = Command('mc {flags} admin user add {target} {username} {password}')
    return cmd(**kwargs)


def admin_user_remove(**kwargs) -> Response:
    '''Remove user on MinIO.

    Usage::

      >>> r = admin_user_remove(target='aliasforhost', username='hellokitten')
      >>> r.content
      [{
       'status': 'success',
       'accessKey': 'hellokitten'
      }]
    '''
    cmd = Command('mc {flags} admin user remove {target} {username}')
    return cmd(**kwargs)


def admin_user_enable(**kwargs) -> Response:
    '''Enable a user on MinIO.

    Usage::

      >>> r = admin_user_enable(target='aliasforhost', username='rockstar')
      >>> r.content
      [{'status': 'success', 'accessKey': 'rockstar'}]
    '''
    cmd = Command('mc {flags} admin user enable {target} {username}')
    return cmd(**kwargs)


def admin_user_disable(**kwargs) -> Response:
    '''Disable a user on MinIO.

    Usage::

      >>> r = admin_user_disable(target='aliasforhost', username='rockstar')
      >>> r.content
      [{'status': 'success', 'accessKey': 'rockstar'}]
    '''
    cmd = Command('mc {flags} admin user disable {target} {username}')
    return cmd(**kwargs)


def admin_user_list(**kwargs) -> Response:
    '''List all users on MinIO.

    Usage::

      >>> admin_admin_user_list(target='aliasforhost')
      >>> r.content
      [{'status': 'success', 'accessKey': 'hellokitten', 'userStatus': 'enabled'},
       {'status': 'success', 'accessKey': 'jumanji', 'userStatus': 'enabled'},
       {'status': 'success', 'accessKey': 'rockstar', 'userStatus': 'enabled'},
       {'status': 'success', 'accessKey': 'test_access_key', 'policyName': 'readwrite', 'userStatus': 'enabled'}]
    '''
    cmd = Command('mc {flags} admin user list {target}')
    return cmd(**kwargs)


def admin_user_info(**kwargs) -> Response:
    '''Display info of a user.

    Usage::

      >>> r = admin_user_info(target='aliasforhost', username='rockstar')
      >>> r.content
      [{'status': 'success', 'accessKey': 'rockstar', 'userStatus': 'disabled'}]
    '''
    cmd = Command('mc {flags} admin user info {target} {username}')
    return cmd(**kwargs)


## svcacct

def admin_user_svcacct_add(**kwargs) -> Response:
    '''Add a new service account for user on MinIO.

    Usage::
      >>> r = admin_user_svcacct_add(
            target: str = 'aliasforhost', 
            username: str = 'rockstar', 
            access_key: Optional[str] = '...', 
            secret_key: Optional[str] = '...', 
            policy: Optional[str] = '...', # path to policy file
        )
      >>> r.content
      [{'status': 'success',
        'accessKey': 'rockstar',
        'secretKey': 'verysecretpassword',
        'userStatus': 'enabled'}]
    '''
    cmdstr = 'mc {flags} admin user svcacct add'
    if 'access_key' in kwargs: cmdstr += ' --access-key {access_key}'
    if 'secret_key' in kwargs: cmdstr += ' --secret-key {secret_key}'
    if 'policy' in kwargs: cmdstr += ' --policy {policy}'
    cmdstr += ' {target} {username}'
    cmd = Command(cmdstr)
    return cmd(**kwargs)


def admin_user_svcacct_remove(**kwargs) -> Response:
    '''Remove a service account on MinIO.

    Usage::

      >>> r = admin_user_svcacct_remove(target='aliasforhost', name='myserviceaccount')
      >>> r.content
      [{
       'status': 'success',
       'accessKey': 'myserviceaccount'
      }]
    '''
    cmd = Command('mc {flags} admin user svcacct remove {target} {name}')
    return cmd(**kwargs)


def admin_user_svcacct_enable(**kwargs) -> Response:
    '''Enable a service account on MinIO.

    Usage::

      >>> r = admin_user_svcacct_enable(target='aliasforhost', name='rockstar')
    '''
    cmd = Command('mc {flags} admin user svcacct enable {target} {name}')
    return cmd(**kwargs)


def admin_user_svcacct_disable(**kwargs) -> Response:
    '''Disable a service account on MinIO.

    Usage::

      >>> r = admin_user_svcacct_disable(target='aliasforhost', username='rockstar')
    '''
    cmd = Command('mc {flags} admin user svcacct disable {target} {name}')
    return cmd(**kwargs)


def admin_user_svcacct_list(**kwargs) -> Response:
    '''List all service accounts on MinIO.

    Usage::

      >>> admin_user_svcacct_list(target='aliasforhost')
    '''
    cmd = Command('mc {flags} admin user svcacct list {target}')
    return cmd(**kwargs)

def admin_user_svcacct_edit(**kwargs) -> Response:
    '''Edit an existing service account on MinIO.

    Usage::
      >>> r = admin_user_svcacct_add(
            target: str = 'aliasforhost', 
            name: str = 'myserviceaccount', 
            secret_key: Optional[str] = '...', 
            policy: Optional[str] = '...', # path to policy file
        )
      >>> r.content
      [{'status': 'success',
        'accessKey': 'rockstar',
        'secretKey': 'verysecretpassword',
        'userStatus': 'enabled'}]
    '''
    cmdstr = 'mc {flags} admin user svcacct edit'
    if 'secret_key' in kwargs: cmdstr += ' --secret-key {secret_key}'
    if 'policy' in kwargs: cmdstr += ' --policy {policy}'
    cmdstr += ' {target} {name}'
    cmd = Command(cmdstr)
    return cmd(**kwargs)


## Async

async def async_admin_user_add(**kwargs) -> Response:
    '''Add a new user on MinIO.

    Usage::

      >>> r = admin_user_add(target='aliasforhost', username='rockstar', password='verysecretpassword')
      >>> r.content
      [{'status': 'success',
        'accessKey': 'rockstar',
        'secretKey': 'verysecretpassword',
        'userStatus': 'enabled'}]
    '''
    cmd = AsyncCommand('mc {flags} admin user add {target} {username} {password}')
    return await cmd.run(**kwargs)


async def async_admin_user_remove(**kwargs) -> Response:
    '''Remove user on MinIO.

    Usage::

      >>> r = admin_user_remove(target='aliasforhost', username='hellokitten')
      >>> r.content
      [{
       'status': 'success',
       'accessKey': 'hellokitten'
      }]
    '''
    cmd = AsyncCommand('mc {flags} admin user remove {target} {username}')
    return await cmd.run(**kwargs)


async def async_admin_user_enable(**kwargs) -> Response:
    '''Enable a user on MinIO.

    Usage::

      >>> r = admin_user_enable(target='aliasforhost', username='rockstar')
      >>> r.content
      [{'status': 'success', 'accessKey': 'rockstar'}]
    '''
    cmd = AsyncCommand('mc {flags} admin user enable {target} {username}')
    return await cmd.run(**kwargs)


async def async_admin_user_disable(**kwargs) -> Response:
    '''Disable a user on MinIO.

    Usage::

      >>> r = admin_user_disable(target='aliasforhost', username='rockstar')
      >>> r.content
      [{'status': 'success', 'accessKey': 'rockstar'}]
    '''
    cmd = AsyncCommand('mc {flags} admin user disable {target} {username}')
    return await cmd.run(**kwargs)

async def async_admin_user_list(**kwargs) -> Response:
    '''List all users on MinIO.

    Usage::

      >>> admin_admin_user_list(target='aliasforhost')
      >>> r.content
      [{'status': 'success', 'accessKey': 'hellokitten', 'userStatus': 'enabled'},
       {'status': 'success', 'accessKey': 'jumanji', 'userStatus': 'enabled'},
       {'status': 'success', 'accessKey': 'rockstar', 'userStatus': 'enabled'},
       {'status': 'success', 'accessKey': 'test_access_key', 'policyName': 'readwrite', 'userStatus': 'enabled'}]
    '''
    cmd = AsyncCommand('mc {flags} admin user list {target}')
    return await cmd.run(**kwargs)

async def async_admin_user_info(**kwargs) -> Response:
    '''Display info of a user.

    Usage::

      >>> r = admin_user_info(target='aliasforhost', username='rockstar')
      >>> r.content
      [{'status': 'success', 'accessKey': 'rockstar', 'userStatus': 'disabled'}]
    '''
    cmd = AsyncCommand('mc {flags} admin user info {target} {username}')
    return await cmd.run(**kwargs)


## svc account


async def async_admin_user_svcacct_add(**kwargs) -> Response:
    '''Add a new service account for user on MinIO.

    Usage::
      >>> r = admin_user_svcacct_add(
            target: str = 'aliasforhost', 
            username: str = 'rockstar', 
            access_key: Optional[str] = '...', 
            secret_key: Optional[str] = '...', 
            policy: Optional[str] = '...', # path to policy file
        )
      >>> r.content
      [{'status': 'success',
        'accessKey': 'rockstar',
        'secretKey': 'verysecretpassword',
        'userStatus': 'enabled'}]
    '''
    cmdstr = 'mc {flags} admin user svcacct add'
    if 'access_key' in kwargs: cmdstr += ' --access-key {access_key}'
    if 'secret_key' in kwargs: cmdstr += ' --secret-key {secret_key}'
    if 'policy' in kwargs: cmdstr += ' --policy {policy}'
    cmdstr += ' {target} {username}'
    cmd = AsyncCommand(cmdstr)
    return await cmd.run(**kwargs)


async def async_admin_user_svcacct_remove(**kwargs) -> Response:
    '''Remove a service account on MinIO.

    Usage::

      >>> r = admin_user_svcacct_remove(target='aliasforhost', name='myserviceaccount')
      >>> r.content
      [{
       'status': 'success',
       'accessKey': 'myserviceaccount'
      }]
    '''
    cmd = AsyncCommand('mc {flags} admin user svcacct remove {target} {name}')
    return await cmd.run(**kwargs)


async def async_admin_user_svcacct_enable(**kwargs) -> Response:
    '''Enable a service account on MinIO.

    Usage::

      >>> r = admin_user_svcacct_enable(target='aliasforhost', name='rockstar')
    '''
    cmd = AsyncCommand('mc {flags} admin user svcacct enable {target} {name}')
    return await cmd.run(**kwargs)


async def async_admin_user_svcacct_disable(**kwargs) -> Response:
    '''Disable a service account on MinIO.

    Usage::

      >>> r = admin_user_svcacct_disable(target='aliasforhost', name='rockstar')
    '''
    cmd = AsyncCommand('mc {flags} admin user svcacct disable {target} {name}')
    return await cmd.run(**kwargs)


async def async_admin_user_svcacct_list(**kwargs) -> Response:
    '''List all service accounts on MinIO.

    Usage::

      >>> admin_user_svcacct_list(target='aliasforhost')
    '''
    cmd = AsyncCommand('mc {flags} admin user svcacct list {target}')
    return await cmd.run(**kwargs)

async def async_admin_user_svcacct_edit(**kwargs) -> Response:
    '''Edit an existing service account on MinIO.

    Usage::
      >>> r = admin_user_svcacct_add(
            target: str = 'aliasforhost', 
            name: str = 'myserviceaccount', 
            secret_key: Optional[str] = '...', 
            policy: Optional[str] = '...', # path to policy file
        )
      >>> r.content
      [{'status': 'success',
        'accessKey': 'rockstar',
        'secretKey': 'verysecretpassword',
        'userStatus': 'enabled'}]
    '''
    cmdstr = 'mc {flags} admin user svcacct edit'
    if 'secret_key' in kwargs: cmdstr += ' --secret-key {secret_key}'
    if 'policy' in kwargs: cmdstr += ' --policy {policy}'
    cmdstr += ' {target} {name}'
    cmd = AsyncCommand(cmdstr)
    return await cmd.run(**kwargs)
