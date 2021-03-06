from schema import Schema, Or

from testrail.models.base import PostModel
from testrail.models.mixins.fields import IdMixin, NameMixin, ProjectIdMixin, ConfigsMixin
from testrail.models.mixins.methods import AddMixin, UpdateMixin, DeleteMixin


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
        'configs': list,
        'id': int,
        'name': str,
        'project_id': int
    })

    def add(self, project_id):
        response = self._add(project_id=project_id)
        return response

    def update(self):
        response = self._add(config_group_id=self.id)
        return response

    def delete(self):
        response = self._delete(config_group_id=self.id)
        return response

