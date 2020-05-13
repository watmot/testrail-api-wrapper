from schema import Schema, Optional, Or, Regex

from testrail.models.base import PostModel
from testrail.models.mixins.fields import (AssignedToIdMixin, BlockedCountMixin, CompletedOnMixin, CreatedByMixin,
                                           CreatedOnMixin, DescriptionMixin, EntriesMixin, FailedCountMixin, IdMixin,
                                           IsCompletedMixin, MilestoneIdMixin, NameMixin, PassedCountMixin,
                                           ProjectIdMixin, RetestCountMixin, UntestedCountMixin, UrlMixin)
from testrail.models.mixins.methods import GetMixin, AddMixin, UpdateMixin, DeleteMixin, CloseMixin


class PlanModel(AssignedToIdMixin, BlockedCountMixin, CompletedOnMixin, CreatedByMixin, CreatedOnMixin,
                DescriptionMixin, EntriesMixin, FailedCountMixin, IdMixin, IsCompletedMixin, MilestoneIdMixin,
                NameMixin, PassedCountMixin, ProjectIdMixin, RetestCountMixin, UntestedCountMixin, UrlMixin,
                DeleteMixin, CloseMixin, UpdateMixin, AddMixin, GetMixin, PostModel):

    ENDPOINTS = {
        'get': 'get_plan/{plan_id}',
        'add': 'add_plan/{project_id}',
        'update': 'update_plan/{plan_id}',
        'delete': 'delete_plan/{plan_id}',
        'close': 'close_plan/{plan_id}'
    }

    POST_FIELDS = {
        'add': [
            'name',
            'description',
            'milestone_id',
            'entries'
        ],
        'update': [
            'name',
            'description',
            'milestone_id'
        ]
    }

    SCHEMA = Schema({
        'assignedto_id': Or(int, None),
        'blocked_count': int,
        'completed_on': Or(int, None),
        'created_by': int,
        'created_on': int,
        'description': Or(str, None),
        'failed_count': int,
        'id': int,
        'is_completed': bool,
        'milestone_id': Or(int, None),
        'name': str,
        'passed_count': int,
        'project_id': int,
        'retest_count': int,
        'untested_count': int,
        'url': str,
        Optional('entries'): list,
        Optional(Regex(r'^custom_status')): int
    })

    def get(self, plan_id):
        response = self._get(plan_id=plan_id)
        return response

    def add(self, project_id):
        response = self._add(project_id=project_id)
        return response

    def update(self):
        response = self._update(plan_id=self.id)
        return response

    def close(self):
        response = self._close(plan_id=self.id)
        return response

    def delete(self):
        response = self._delete(plan_id=self.id)
        return response
