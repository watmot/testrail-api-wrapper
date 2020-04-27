from schema import Schema, Or

from testrail.models.base import PostModel

from testrail.models.mixins.fields.id import IdMixin
from testrail.models.mixins.fields.name import NameMixin
from testrail.models.mixins.fields.project_id import ProjectIdMixin
from testrail.models.mixins.fields.configs import ConfigsMixin

from testrail.models.mixins.methods.add import AddMixin
from testrail.models.mixins.methods.update import UpdateMixin
from testrail.models.mixins.methods.delete import DeleteMixin


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

