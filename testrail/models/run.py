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
from testrail.models.mixins.fields.include_all import IncludeAllMixin
from testrail.models.mixins.fields.is_completed import IsCompletedMixin
from testrail.models.mixins.fields.milestone_id import MilestoneIdMixin
from testrail.models.mixins.fields.name import NameMixin
from testrail.models.mixins.fields.passed_count import PassedCountMixin
from testrail.models.mixins.fields.project_id import ProjectIdMixin
from testrail.models.mixins.fields.retest_count import RetestCountMixin
from testrail.models.mixins.fields.suite_id import SuiteIdMixin
from testrail.models.mixins.fields.untested_count import UntestedCountMixin
from testrail.models.mixins.fields.url import UrlMixin

from testrail.models.mixins.methods.get import GetMixin
from testrail.models.mixins.methods.add import AddMixin
from testrail.models.mixins.methods.update import UpdateMixin
from testrail.models.mixins.methods.delete import DeleteMixin
from testrail.models.mixins.methods.close import CloseMixin


class RunModel(AssignedToIdMixin, BlockedCountMixin, CompletedOnMixin, CreatedByMixin, CreatedOnMixin,
               CustomStatus1CountMixin, CustomStatus2CountMixin, CustomStatus3CountMixin, CustomStatus4CountMixin,
               CustomStatus5CountMixin, CustomStatus6CountMixin, CustomStatus7CountMixin, DescriptionMixin,
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
        'custom_status1_count': int,
        'custom_status2_count': int,
        'custom_status3_count': int,
        'custom_status4_count': int,
        'custom_status5_count': int,
        'custom_status6_count': int,
        'custom_status7_count': int,
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
        'refs': Or(None, str)
    })

    def get(self, run_id):
        response = self._get(run_id=run_id)
        self._update_data(response)
        return response

    def add(self, project_id):
        response = self._add(project_id=project_id)
        self._update_data(response)
        return response

    def update(self):
        response = self._update(run_id=self.id)
        self._update_data(response)
        return response

    def close(self):
        response = self._close(run_id=self.id)
        self._update_data(response)
        return response

    def delete(self):
        response = self._delete(run_id=self.id)
        return response
