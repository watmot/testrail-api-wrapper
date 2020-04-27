from schema import Schema, Or

from testrail.models.base import PostModel
from testrail.models.mixins.fields.announcement import AnnouncementMixin
from testrail.models.mixins.fields.completed_on import CompletedOnMixin
from testrail.models.mixins.fields.id import IdMixin
from testrail.models.mixins.fields.is_completed import IsCompletedMixin
from testrail.models.mixins.fields.name import NameMixin
from testrail.models.mixins.fields.show_announcement import ShowAnnouncementMixin
from testrail.models.mixins.fields.suite_mode import SuiteModeMixin
from testrail.models.mixins.fields.url import UrlMixin
from testrail.models.mixins.methods.get import GetMixin
from testrail.models.mixins.methods.add import AddMixin
from testrail.models.mixins.methods.update import UpdateMixin
from testrail.models.mixins.methods.delete import DeleteMixin


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
        'announcement': str,
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
        self._update_data(response)
        return response

    def add(self):
        response = self._add()
        self._update_data(response)
        return response

    def update(self):
        response = self._update(project_id=self.id)
        self._update_data(response)
        return response

    def delete(self):
        response = self._delete(project_id=self.id)
        return response
