'''MinIO server. restart and stop all MinIO servers'''

from aiomc.utils import *

__all__ = [
    'restart_service',
    'stop_service',
    'async_restart_service',
    'async_stop_service',
]


def restart_service(**kwargs) -> Response:
    '''Restart object storage server.

    Usage::

      >>> restart_service(target='aliasforhost')
    '''
    cmd = Command('minio {flags} service restart {target}')
    return cmd(**kwargs)


def stop_service(**kwargs) -> Response:
    '''Stop object storage server.

    Usage::

      >>> stop_service(target='aliasforhost')
    '''
    cmd = Command('minio {flags} service stop {target}')
    return cmd(**kwargs)


async def async_restart_service(**kwargs) -> Response:
    '''Restart object storage server

    Usage::

      >>> async_restart_service(target='aliasforhost')
    '''
    cmd = AsyncCommand('minio {flags} service restart {target}')
    return await cmd.run(**kwargs)

async def async_stop_service(**kwargs) -> Response:
    '''Stop object storage server

    Usage::

      >>> stop_service(target='aliasforhost')
    '''
    cmd = AsyncCommand('minio {flags} service stop {target}')
    return await cmd.run(**kwargs)

