from schema import Schema, Or

from testrail.models.base import PostModel

from testrail.models.mixins.fields import IdMixin
from testrail.models.mixins.fields import NameMixin
from testrail.models.mixins.fields import ProjectIdMixin
from testrail.models.mixins.fields import ConfigsMixin

from testrail.models.mixins.methods import AddMixin
from testrail.models.mixins.methods import UpdateMixin
from testrail.models.mixins.methods import DeleteMixin


class ConfigGroupModel(IdMixin, NameMixin, ProjectIdMixin, ConfigsMixin, DeleteMixin, UpdateMixin, AddMixin, PostModel):

    ENDPOINTS = {
        'add': 'add_config_group/{project_id}',
        'update': 'update_config_group/{config_group_id}',
        'delete': 'delete_config_group/{config_group_id}',
    }

    POST_FIELDS = {
        'add': [
            'name'
        ],
        'update': [
            'name'
        ]
    }

    SCHEMA = Schema({
        'configs': Or(list, None),
        'id': int,
        'name': str,
        'project_id': int
    })

