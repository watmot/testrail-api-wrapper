from schema import Schema

from testrail.models.base import PostModel

from testrail.models.mixins.fields.group_id import GroupIdMixin
from testrail.models.mixins.fields.id import IdMixin
from testrail.models.mixins.fields.name import NameMixin

from testrail.models.mixins.methods.add import AddMixin
from testrail.models.mixins.methods.update import UpdateMixin
from testrail.models.mixins.methods.delete import DeleteMixin


class ConfigModel(GroupIdMixin, IdMixin, NameMixin, DeleteMixin, UpdateMixin, AddMixin, PostModel):

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
        'group_id': int,
        'id': int,
        'name': str
    })
