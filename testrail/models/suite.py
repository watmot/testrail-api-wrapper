from schema import Schema, Or

from testrail.models.base import PostModel

from testrail.models.mixins.fields.completed_on import CompletedOnMixin
from testrail.models.mixins.fields.description import DescriptionMixin
from testrail.models.mixins.fields.id import IdMixin
from testrail.models.mixins.fields.is_baseline import IsBaselineMixin
from testrail.models.mixins.fields.is_completed import IsCompletedMixin
from testrail.models.mixins.fields.is_master import IsMasterMixin
from testrail.models.mixins.fields.name import NameMixin
from testrail.models.mixins.fields.project_id import ProjectIdMixin
from testrail.models.mixins.fields.url import UrlMixin

from testrail.models.mixins.methods.get import GetMixin
from testrail.models.mixins.methods.add import AddMixin
from testrail.models.mixins.methods.update import UpdateMixin
from testrail.models.mixins.methods.delete import DeleteMixin


class SuiteModel(CompletedOnMixin, DescriptionMixin, IdMixin, IsBaselineMixin, IsCompletedMixin, IsMasterMixin,
                 NameMixin, ProjectIdMixin, UrlMixin, DeleteMixin, UpdateMixin, AddMixin, GetMixin, PostModel):

    ENDPOINTS = {
        'get': 'get_suite/{suite_id}',
        'add': 'add_suite/{project_id}',
        'update': 'update_suite/{suite_id}',
        'delete': 'delete_suite/{suite_id}',
    }

    POST_FIELDS = {
        'add': [
            'name',
            'description'
        ],
        'update': [
            'name',
            'description'
        ]
    }

    SCHEMA = Schema({
        'completed_on': Or(str, None),
        'description': str,
        'id': int,
        'is_baseline': bool,
        'is_completed': bool,
        'is_master': bool,
        'name': str,
        'project_id': int,
        'url': str
    })

    def get(self, suite_id):
        response = self._get(suite_id=suite_id)
        self._update_data(response)
        return response

    def add(self, project_id):
        response = self._add(project_id=project_id)
        self._update_data(response)
        return response

    def update(self):
        response = self._update(suite_id=self.id)
        self._update_data(response)
        return response

    def delete(self):
        response = self._delete(suite_id=self.id)
        return response
