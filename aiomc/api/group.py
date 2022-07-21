from aiomc.utils import *

__all__ = [
    'admin_group_add',
    'admin_group_remove',
    'admin_group_info',
    'admin_group_list',
    'admin_group_enable',
    'admin_group_disable',
    # Async
    'async_admin_group_add',
    'async_admin_group_remove',
    'async_admin_group_info',
    'async_admin_group_list',
    'async_admin_group_enable',
    'async_admin_group_disable',
]

GROUP_COMMAND = 'mc {flags} admin group '


def admin_group_add(**kwargs) -> Response:
    '''Add users to a new or existing group.

    Usage:

      >>> r = admin_group_add(target='aliasforhost', group='admins', members=['rockstar', 'test'])
      >>> r.content
      {'status': 'success', 'groupName': 'admins', 'members': ['rockstar', 'test']}
    '''
    if not isinstance(kwargs['members'], str):
        kwargs['members'] = ' '.join(kwargs['members'])

    cmd = Command(GROUP_COMMAND + 'add {target} {group} {members}')

    return cmd(**kwargs)


def admin_group_remove(**kwargs) -> Response:
    '''Remove group or members from a group.

    Usage::

      >>> r = admin_group_remove(target='aliasforhost', group='admins',
                                members=['rockstar', 'test'])
      >>> r.content
      {'status': 'success', 'groupName': 'admins', 'members': ['rockstar', 'test']}

      >>> r = admin_group_remove(target='local', group='admins')
      >>> r.content
      {'status': 'success', 'groupName': 'admins'}
    '''
    if 'members' not in kwargs:
        kwargs['members'] = ''
    elif not isinstance(kwargs['members'], str):
        kwargs['members'] = ' '.join(kwargs['members'])

    cmd = Command(GROUP_COMMAND + 'remove {target} {group} {members}')

    return cmd(**kwargs)


def admin_group_info(**kwargs) -> Response:
    '''Display group info.

    Usage::

      >>> r = admin_group_info(target='aliasforhost', group='admins')
      >>> r.content
      {'status': 'success', 'groupName': 'admins', 'members': ['rockstar', 'test'],
      'groupStatus': 'enabled', 'groupPolicy': 'somePolicy'}
    '''
    cmd = Command(GROUP_COMMAND + 'info {target} {group}')
    return cmd(**kwargs)


def admin_group_list(**kwargs) -> Response:
    '''Display list of groups.

    Usage::

      >>> r = admin_group_list(target='aliasforhost')
      >>> r.content
      {'status': 'success', 'groups': ['foo', 'bar', 'admins']}
    '''
    cmd = Command(GROUP_COMMAND + 'list {target}')
    return cmd(**kwargs)


def admin_group_enable(**kwargs) -> Response:
    '''Enable a group.

    Usage::

      >>> r = admin_group_enable(target='aliasforhost', group='admins')
      >>> r.content
      {'status': 'success', 'groupName': 'admins', 'groupStatus': 'enabled'}
    '''
    cmd = Command(GROUP_COMMAND + 'enable {target} {group}')
    return cmd(**kwargs)


def admin_group_disable(**kwargs) -> Response:
    '''Disable a group.

    Usage::

      >>> r = admin_group_disable(target='aliasforhost', group='admins')
      >>> r.content
      {'status': 'success', 'groupName': 'admins', 'groupStatus': 'disabled'}
    '''
    cmd = Command(GROUP_COMMAND + 'disable {target} {group}')
    return cmd(**kwargs)

## Async



async def async_admin_group_add(**kwargs) -> Response:
    '''Add users to a new or existing group.

    Usage:

      >>> r = admin_group_add(target='aliasforhost', group='admins', members=['rockstar', 'test'])
      >>> r.content
      {'status': 'success', 'groupName': 'admins', 'members': ['rockstar', 'test']}
    '''
    if not isinstance(kwargs['members'], str):
        kwargs['members'] = ' '.join(kwargs['members'])

    cmd = AsyncCommand(GROUP_COMMAND + 'add {target} {group} {members}')

    return await cmd.run(**kwargs)


async def async_admin_group_remove(**kwargs) -> Response:
    '''Remove group or members from a group.

    Usage::

      >>> r = admin_group_remove(target='aliasforhost', group='admins',
                                members=['rockstar', 'test'])
      >>> r.content
      {'status': 'success', 'groupName': 'admins', 'members': ['rockstar', 'test']}

      >>> r = admin_group_remove(target='local', group='admins')
      >>> r.content
      {'status': 'success', 'groupName': 'admins'}
    '''
    if 'members' not in kwargs:
        kwargs['members'] = ''
    elif not isinstance(kwargs['members'], str):
        kwargs['members'] = ' '.join(kwargs['members'])

    cmd = AsyncCommand(GROUP_COMMAND + 'remove {target} {group} {members}')
    return await cmd.run(**kwargs)


async def async_admin_group_info(**kwargs) -> Response:
    '''Display group info.

    Usage::

      >>> r = admin_group_info(target='aliasforhost', group='admins')
      >>> r.content
      {'status': 'success', 'groupName': 'admins', 'members': ['rockstar', 'test'],
      'groupStatus': 'enabled', 'groupPolicy': 'somePolicy'}
    '''
    cmd = AsyncCommand(GROUP_COMMAND + 'info {target} {group}')
    return await cmd.run(**kwargs)


async def async_admin_group_list(**kwargs) -> Response:
    '''Display list of groups.

    Usage::

      >>> r = admin_group_list(target='aliasforhost')
      >>> r.content
      {'status': 'success', 'groups': ['foo', 'bar', 'admins']}
    '''
    cmd = AsyncCommand(GROUP_COMMAND + 'list {target}')
    return await cmd.run(**kwargs)


async def async_admin_group_enable(**kwargs) -> Response:
    '''Enable a group.

    Usage::

      >>> r = admin_group_enable(target='aliasforhost', group='admins')
      >>> r.content
      {'status': 'success', 'groupName': 'admins', 'groupStatus': 'enabled'}
    '''
    cmd = AsyncCommand(GROUP_COMMAND + 'enable {target} {group}')
    return await cmd.run(**kwargs)



async def async_admin_group_disable(**kwargs) -> Response:
    '''Disable a group.

    Usage::

      >>> r = admin_group_disable(target='aliasforhost', group='admins')
      >>> r.content
      {'status': 'success', 'groupName': 'admins', 'groupStatus': 'disabled'}
    '''
    cmd = AsyncCommand(GROUP_COMMAND + 'disable {target} {group}')
    return await cmd.run(**kwargs)
