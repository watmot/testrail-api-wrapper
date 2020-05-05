from schema import Schema, Or

from testrail.models.base import PostModel

from testrail.models.mixins.fields import CompletedOnMixin
from testrail.models.mixins.fields import DescriptionMixin
from testrail.models.mixins.fields import IdMixin
from testrail.models.mixins.fields import IsBaselineMixin
from testrail.models.mixins.fields import IsCompletedMixin
from testrail.models.mixins.fields import IsMasterMixin
from testrail.models.mixins.fields import NameMixin
from testrail.models.mixins.fields import ProjectIdMixin
from testrail.models.mixins.fields import UrlMixin

from testrail.models.mixins.methods import GetMixin
from testrail.models.mixins.methods import AddMixin
from testrail.models.mixins.methods import UpdateMixin
from testrail.models.mixins.methods import DeleteMixin


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
        return response

    def add(self, project_id):
        response = self._add(project_id=project_id)
        return response

    def update(self):
        response = self._update(suite_id=self.id)
        return response

    def delete(self):
        response = self._delete(suite_id=self.id)
        return response
