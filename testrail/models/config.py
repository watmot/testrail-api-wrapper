from schema import Schema

from testrail.models.base import PostModel
from testrail.models.mixins.fields import GroupIdMixin, IdMixin, NameMixin
from testrail.models.mixins.methods import AddMixin, UpdateMixin, DeleteMixin


class ConfigModel(GroupIdMixin, IdMixin, NameMixin, DeleteMixin, UpdateMixin, AddMixin, PostModel):

    ENDPOINTS = {
        'add': 'add_config/{config_group_id}',
        'update': 'update_config/{config_group_id}',
        'delete': 'delete_config/{config_group_id}',
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

    def add(self, config_group_id):
        response = self._add(config_group_id=config_group_id)
        return response

    def update(self):
        response = self._add(config_group_id=self.group_id)
        return response

    def delete(self):
        response = self._delete(config_group_id=self.group_id)
        return response
