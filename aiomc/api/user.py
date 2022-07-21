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
