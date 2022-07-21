'''MinIO server. Start object storage server'''

from aiomc.utils import *

__all__ = [

    'server',
]


def server(**kwargs) -> Response:
    '''Start object storage server.

    Usage::

      >>> server(address=':9008', dir='/home/jugurtha/data')
    '''
    cmd = Command('minio {flags} server {dir}')
    return cmd(**kwargs)

async def async_server(**kwargs) -> Response:
    '''Start object storage server.

    Usage::

      >>> server(address=':9008', dir='/home/jugurtha/data')
    '''
    cmd = AsyncCommand('minio {flags} server {dir}')
    return await cmd.run(**kwargs)
