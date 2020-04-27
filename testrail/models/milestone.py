from schema import Schema, Or

from testrail.models.base import BaseModel

from testrail.models.mixins.fields.completed_on import CompletedOnMixin
from testrail.models.mixins.fields.description import DescriptionMixin
from testrail.models.mixins.fields.due_on import DueOnMixin
from testrail.models.mixins.fields.id import IdMixin
from testrail.models.mixins.fields.name import NameMixin
from testrail.models.mixins.fields.is_completed import IsCompletedMixin
from testrail.models.mixins.fields.is_started import IsStartedMixin
from testrail.models.mixins.fields.parent_id import ParentIdMixin
from testrail.models.mixins.fields.project_id import ProjectIdMixin
from testrail.models.mixins.fields.start_on import StartOnMixin
from testrail.models.mixins.fields.started_on import StartedOnMixin
from testrail.models.mixins.fields.url import UrlMixin

from testrail.models.mixins.methods.get import GetMixin
from testrail.models.mixins.methods.add import AddMixin
from testrail.models.mixins.methods.update import UpdateMixin
from testrail.models.mixins.methods.delete import DeleteMixin


class MilestoneModel(CompletedOnMixin, DescriptionMixin, DueOnMixin, IdMixin, IsCompletedMixin,  IsStartedMixin,
                     NameMixin, ParentIdMixin, ProjectIdMixin, StartOnMixin, StartedOnMixin, UrlMixin, DeleteMixin,
                     UpdateMixin, AddMixin, GetMixin, BaseModel):

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
        'completed_on': Or(str, None),
        'description': str,
        'due_on': Or(str, None),
        'id': int,
        'is_completed': bool,
        'is_started': bool,
        'milestones': Or(list, None),
        'name': str,
        'parent_id': Or(int, None),
        'project_id': int,
        'start_on': str,
        'started_on': Or(str, None),
        'url': str
    })

    def get(self, milestone_id):
        response = self._get(milestone_id=milestone_id)
        self._update_data(response)

    def add(self, project_id):
        response = self._add(project_id=project_id)
        self._update_data(response)

    def update(self):
        response = self._update(milestone_id=self.id)
        self._update_data(response)

    def delete(self):
        self._delete(milestone_id=self.id)
