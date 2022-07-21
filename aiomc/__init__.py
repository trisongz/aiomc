'''Async Python wrapper for the MinIO command line interface.'''

__version__ = '0.0.1'
__title__ = 'aiomc'


from .api.ls import (
    ls,
    async_ls,
)

from .api.mb import (
    mb,
    async_mb
)

from .api.rb import (
    rb,
    async_rb
)

from .api.cp import (
    cp,
    async_cp
)


from .api.user import (
    admin_user_list,
    admin_user_add,
    admin_user_remove,
    admin_user_enable,
    admin_user_disable,
    admin_user_info,
    # Async
    async_admin_user_list,
    async_admin_user_add,
    async_admin_user_remove,
    async_admin_user_enable,
    async_admin_user_disable,
    async_admin_user_info,
)

from .api.config import (
    config_host_add,
    config_host_list,
    async_config_host_add,
    async_config_host_list,
    
)


from .api.server import (
    server,
    async_server
)

from .api.policy import (
    admin_policy_add,
    admin_policy_remove,
    admin_policy_list,
    admin_policy_info,
    admin_policy_set,
    async_admin_policy_add,
    async_admin_policy_remove,
    async_admin_policy_list,
    async_admin_policy_info,
    async_admin_policy_set,
)

from .api.group import (
    admin_group_add,
    admin_group_remove,
    admin_group_info,
    admin_group_list,
    admin_group_enable,
    admin_group_disable,
    async_admin_group_add,
    async_admin_group_remove,
    async_admin_group_info,
    async_admin_group_list,
    async_admin_group_enable,
    async_admin_group_disable,
)

from .utils import (
    aiomcError,
    check_error,
    mc_binary_path,
)

assert mc_binary_path is not None, 'Unable to locate the `mc` binary required to run this module.'
print(f'Using `mc` from: {mc_binary_path}')
