from schema import Schema, Or, Optional, Regex

from testrail.models.base import PostModel
from testrail.models.mixins.fields import (AssignedToIdMixin, BlockedCountMixin, CompletedOnMixin, CreatedByMixin,
                                           CreatedOnMixin, DescriptionMixin, FailedCountMixin, IdMixin, IncludeAllMixin,
                                           IsCompletedMixin, MilestoneIdMixin, NameMixin, PassedCountMixin,
                                           ProjectIdMixin, RetestCountMixin, SuiteIdMixin, UntestedCountMixin, UrlMixin)
from testrail.models.mixins.methods import CloseMixin, DeleteMixin, UpdateMixin, AddMixin, GetMixin


class RunModel(AssignedToIdMixin, BlockedCountMixin, CompletedOnMixin, CreatedByMixin, CreatedOnMixin, DescriptionMixin,
               FailedCountMixin, IdMixin, IncludeAllMixin, IsCompletedMixin, MilestoneIdMixin, NameMixin,
               PassedCountMixin, ProjectIdMixin, RetestCountMixin, SuiteIdMixin, UntestedCountMixin, UrlMixin,
               CloseMixin, DeleteMixin, UpdateMixin, AddMixin, GetMixin, PostModel):

    ENDPOINTS = {
        'get': 'get_run/{run_id}',
        'add': 'add_run/{project_id}',
        'update': 'update_run/{run_id}',
        'delete': 'delete_run/{run_id}',
        'close': 'close_run/{run_id}'
    }

    POST_FIELDS = {
        'add': [
            'suite_id',
            'name',
            'description',
            'milestone_id',
            'assignedto_id',
            'include_all'
        ],
        'update': [
            'name',
            'description',
            'milestone_id',
            'include_all'
        ]
    }

    SCHEMA = Schema({
        'assignedto_id': Or(int, None),
        'blocked_count': int,
        'completed_on': Or(int, None),
        'config': Or(str, None),
        'config_ids': Or(list, None),
        'created_by': int,
        'created_on': int,
        'description': Or(str, None),
        'failed_count': int,
        'id': int,
        'include_all': bool,
        'is_completed': bool,
        'milestone_id': Or(int, None),
        'plan_id': Or(int, None),
        'name': str,
        'passed_count': int,
        'project_id': int,
        'retest_count': int,
        'suite_id': int,
        'untested_count': int,
        'url': str,
        'refs': Or(None, str),
        Optional(Regex(r'^custom_status')): int
    })

    def get(self, run_id):
        response = self._get(run_id=run_id)
        return response

    def add(self, project_id):
        response = self._add(project_id=project_id)
        return response

    def update(self):
        response = self._update(run_id=self.id)
        return response

    def close(self):
        response = self._close(run_id=self.id)
        return response

    def delete(self):
        response = self._delete(run_id=self.id)
        return response
