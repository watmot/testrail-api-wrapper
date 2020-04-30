from schema import Schema, Or

from testrail.models.base import PostModel

from testrail.models.mixins.fields.assignedto_id import AssignedToIdMixin
from testrail.models.mixins.fields.blocked_count import BlockedCountMixin
from testrail.models.mixins.fields.completed_on import CompletedOnMixin
from testrail.models.mixins.fields.created_by import CreatedByMixin
from testrail.models.mixins.fields.created_on import CreatedOnMixin
from testrail.models.mixins.fields.custom_status_1_count import CustomStatus1CountMixin
from testrail.models.mixins.fields.custom_status_2_count import CustomStatus2CountMixin
from testrail.models.mixins.fields.custom_status_3_count import CustomStatus3CountMixin
from testrail.models.mixins.fields.custom_status_4_count import CustomStatus4CountMixin
from testrail.models.mixins.fields.custom_status_5_count import CustomStatus5CountMixin
from testrail.models.mixins.fields.custom_status_6_count import CustomStatus6CountMixin
from testrail.models.mixins.fields.custom_status_7_count import CustomStatus7CountMixin
from testrail.models.mixins.fields.description import DescriptionMixin
from testrail.models.mixins.fields.failed_count import FailedCountMixin
from testrail.models.mixins.fields.id import IdMixin
from testrail.models.mixins.fields.is_completed import IsCompletedMixin
from testrail.models.mixins.fields.milestone_id import MilestoneIdMixin
from testrail.models.mixins.fields.name import NameMixin
from testrail.models.mixins.fields.passed_count import PassedCountMixin
from testrail.models.mixins.fields.project_id import ProjectIdMixin
from testrail.models.mixins.fields.retest_count import RetestCountMixin
from testrail.models.mixins.fields.untested_count import UntestedCountMixin
from testrail.models.mixins.fields.url import UrlMixin

from testrail.models.mixins.methods.get import GetMixin
from testrail.models.mixins.methods.add import AddMixin
from testrail.models.mixins.methods.update import UpdateMixin
from testrail.models.mixins.methods.delete import DeleteMixin
from testrail.models.mixins.methods.close import CloseMixin


class PlanModel(AssignedToIdMixin, BlockedCountMixin, CompletedOnMixin, CreatedByMixin, CreatedOnMixin,
                CustomStatus1CountMixin, CustomStatus2CountMixin, CustomStatus3CountMixin, CustomStatus4CountMixin,
                CustomStatus5CountMixin, CustomStatus6CountMixin, CustomStatus7CountMixin, DescriptionMixin,
                FailedCountMixin, IdMixin, IsCompletedMixin, MilestoneIdMixin, NameMixin, PassedCountMixin,
                ProjectIdMixin, RetestCountMixin, UntestedCountMixin, UrlMixin, DeleteMixin, CloseMixin, UpdateMixin,
                AddMixin, GetMixin, PostModel):

    ENDPOINTS = {
        'get': 'get_plan/{plan_id}',
        'get_collection': 'get_plans/{project_id}{params}',
        'add': 'add_plan/{project_id}',
        'update': 'update_plan/{plan_id}',
        'delete': 'delete_plan/{plan_id}',
        'close': 'close_plan/{plan_id}'
    }

    POST_FIELDS = {
        'add': [
            'name',
            'description',
            'milestone_id'
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
        'custom_status1_count': int,
        'custom_status2_count': int,
        'custom_status3_count': int,
        'custom_status4_count': int,
        'custom_status5_count': int,
        'custom_status6_count': int,
        'custom_status7_count': int,
        'description': Or(str, None),
        'entries': Or(list, None),
        'failed_count': int,
        'id': int,
        'is_completed': bool,
        'milestone_id': Or(int, None),
        'name': str,
        'passed_count': int,
        'project_id': int,
        'retest_count': int,
        'untested_count': int,
        'url': str
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
