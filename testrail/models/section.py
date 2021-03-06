from schema import Schema, Or

from testrail.models.base import PostModel
from testrail.models.mixins.fields import (DepthMixin, DescriptionMixin, DisplayOrderMixin, IdMixin, ParentIdMixin,
                                           ProjectIdMixin, NameMixin, SuiteIdMixin)
from testrail.models.mixins.methods import DeleteMixin, AddMixin, UpdateMixin, GetMixin


class SectionModel(DepthMixin, DescriptionMixin, DisplayOrderMixin, IdMixin, ParentIdMixin, ProjectIdMixin, NameMixin,
                   SuiteIdMixin, DeleteMixin, AddMixin, UpdateMixin, GetMixin, PostModel):

    ENDPOINTS = {
        'get': 'get_section/{section_id}',
        'add': 'add_section/{project_id}',
        'update': 'update_section/{section_id}',
        'delete': 'delete_section/{section_id}',
    }

    POST_FIELDS = {
        'add': [
            'description',
            'suite_id',
            'parent_id',
            'name'
        ],
        'update': [
            'description',
            'name'
        ]
    }

    SCHEMA = Schema({
        'depth': int,
        'description': Or(str, None),
        'display_order': int,
        'id': int,
        'parent_id': Or(int, None),
        'name': str,
        'suite_id': int
    })

    def get(self, section_id):
        response = self._get(section_id=section_id)
        return response

    def add(self, project_id):
        response = self._add(project_id=project_id)
        return response

    def update(self):
        response = self._update(section_id=self.id)
        return response

    def delete(self):
        response = self._delete(section_id=self.id)
        return response
