from schema import Schema, Or

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
from testrail.models.mixins.fields import IncludeAllMixin
from testrail.models.mixins.fields import IsCompletedMixin
from testrail.models.mixins.fields import MilestoneIdMixin
from testrail.models.mixins.fields import NameMixin
from testrail.models.mixins.fields import PassedCountMixin
from testrail.models.mixins.fields import ProjectIdMixin
from testrail.models.mixins.fields import RetestCountMixin
from testrail.models.mixins.fields import SuiteIdMixin
from testrail.models.mixins.fields import UntestedCountMixin
from testrail.models.mixins.fields import UrlMixin

from testrail.models.mixins.methods import GetMixin
from testrail.models.mixins.methods import AddMixin
from testrail.models.mixins.methods import UpdateMixin
from testrail.models.mixins.methods import DeleteMixin
from testrail.models.mixins.methods import CloseMixin


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
