from schema import Schema, Or

from testrail.models.base import PostModel
from testrail.models.mixins.fields import (AnnouncementMixin, CompletedOnMixin, IdMixin, IsCompletedMixin, NameMixin,
                                           ShowAnnouncementMixin, SuiteModeMixin, UrlMixin)
from testrail.models.mixins.methods import GetMixin, AddMixin, UpdateMixin, DeleteMixin


class ProjectModel(AnnouncementMixin, CompletedOnMixin, IdMixin, IsCompletedMixin, NameMixin, ShowAnnouncementMixin,
                   SuiteModeMixin, UrlMixin, DeleteMixin, UpdateMixin, AddMixin, GetMixin, PostModel):

    ENDPOINTS = {
        'get': 'get_project/{project_id}',
        'add': 'add_project',
        'update': 'update_project/{project_id}',
        'delete': 'delete_project/{project_id}',
    }

    POST_FIELDS = {
        'add': [
            'name',
            'announcement',
            'show_announcement',
            'suite_mode'
        ],
        'update': [
            'is_completed'
        ]
    }

    SCHEMA = Schema({
        'announcement': Or(str, None),
        'completed_on': Or(int, None),
        'id': int,
        'is_completed': bool,
        'name': str,
        'show_announcement': bool,
        'suite_mode': int,
        'url': str
    })

    def get(self, project_id):
        response = self._get(project_id=project_id)
        return response

    def add(self):
        response = self._add()
        return response

    def update(self):
        response = self._update(project_id=self.id)
        return response

    def delete(self):
        response = self._delete(project_id=self.id)
        return response
