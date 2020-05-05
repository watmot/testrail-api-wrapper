from schema import Schema, Or

from testrail.models.base import BaseModel

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


class TestModel(CompletedOnMixin, DescriptionMixin, IdMixin, IsBaselineMixin, IsCompletedMixin, IsMasterMixin,
                 NameMixin, ProjectIdMixin, UrlMixin, GetMixin, BaseModel):

    ENDPOINTS = {
        'get': 'get_suite/{suite_id}',
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
