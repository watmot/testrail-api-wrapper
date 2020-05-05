from schema import Schema, Optional, Or

from testrail.models.base import PostModel

from testrail.models.mixins.fields import CompletedOnMixin
from testrail.models.mixins.fields import DescriptionMixin
from testrail.models.mixins.fields import DueOnMixin
from testrail.models.mixins.fields import IdMixin
from testrail.models.mixins.fields import NameMixin
from testrail.models.mixins.fields import IsCompletedMixin
from testrail.models.mixins.fields import IsStartedMixin
from testrail.models.mixins.fields import ParentIdMixin
from testrail.models.mixins.fields import ProjectIdMixin
from testrail.models.mixins.fields import StartOnMixin
from testrail.models.mixins.fields import StartedOnMixin
from testrail.models.mixins.fields import UrlMixin

from testrail.models.mixins.methods import GetMixin
from testrail.models.mixins.methods import AddMixin
from testrail.models.mixins.methods import UpdateMixin
from testrail.models.mixins.methods import DeleteMixin


class MilestoneModel(CompletedOnMixin, DescriptionMixin, DueOnMixin, IdMixin, IsCompletedMixin,  IsStartedMixin,
                     NameMixin, ParentIdMixin, ProjectIdMixin, StartOnMixin, StartedOnMixin, UrlMixin, DeleteMixin,
                     UpdateMixin, AddMixin, GetMixin, PostModel):

    ENDPOINTS = {
        'get': 'get_milestone/{milestone_id}',
        'add': 'add_milestone/{project_id}',
        'update': 'update_milestone/{milestone_id}',
        'delete': 'delete_milestone/{milestone_id}'
    }

    POST_FIELDS = {
        'add': [
            'name',
            'description',
            'due_on',
            'parent_id',
            'start_on'
        ],
        'update': [
            'is_completed',
            'is_started',
            'parent_id',
            'start_on'
        ]
    }

    SCHEMA = Schema({
        'completed_on': Or(int, None),
        'description': str,
        'due_on': Or(int, None),
        'id': int,
        'is_completed': bool,
        'is_started': bool,
        Optional('milestones'): Or(list, None),
        'name': str,
        'parent_id': Or(int, None),
        'project_id': int,
        'start_on': int,
        'started_on': Or(int, None),
        'url': str
    })

    def get(self, milestone_id):
        response = self._get(milestone_id=milestone_id)
        return response

    def add(self, project_id):
        response = self._add(project_id=project_id)
        return response

    def update(self):
        response = self._update(milestone_id=self.id)
        return response

    def delete(self):
        response = self._delete(milestone_id=self.id)
        return response
