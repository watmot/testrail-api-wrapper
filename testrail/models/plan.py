from schema import Schema, Optional, Or

from testrail.models.base import PostModel

from testrail.models.mixins.fields import AssignedToIdMixin
from testrail.models.mixins.fields import BlockedCountMixin
from testrail.models.mixins.fields import CompletedOnMixin
from testrail.models.mixins.fields import CreatedByMixin
from testrail.models.mixins.fields import CreatedOnMixin
from testrail.models.mixins.fields import CustomStatus1CountMixin
from testrail.models.mixins.fields import CustomStatus2CountMixin
from testrail.models.mixins.fields import CustomStatus3CountMixin
from testrail.models.mixins.fields import CustomStatus4CountMixin
from testrail.models.mixins.fields import CustomStatus5CountMixin
from testrail.models.mixins.fields import CustomStatus6CountMixin
from testrail.models.mixins.fields import CustomStatus7CountMixin
from testrail.models.mixins.fields import DescriptionMixin
from testrail.models.mixins.fields import FailedCountMixin
from testrail.models.mixins.fields import IdMixin
from testrail.models.mixins.fields import IsCompletedMixin
from testrail.models.mixins.fields import MilestoneIdMixin
from testrail.models.mixins.fields import NameMixin
from testrail.models.mixins.fields import PassedCountMixin
from testrail.models.mixins.fields import ProjectIdMixin
from testrail.models.mixins.fields import RetestCountMixin
from testrail.models.mixins.fields import UntestedCountMixin
from testrail.models.mixins.fields import UrlMixin

from testrail.models.mixins.methods import GetMixin
from testrail.models.mixins.methods import AddMixin
from testrail.models.mixins.methods import UpdateMixin
from testrail.models.mixins.methods import DeleteMixin
from testrail.models.mixins.methods import CloseMixin


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
        Optional('entries'): Or(list, None),
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
