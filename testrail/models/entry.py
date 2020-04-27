from schema import Schema, Or

from testrail.models.base import PostModel

from testrail.models.mixins.fields.suite_id import SuiteIdMixin
from testrail.models.mixins.fields.name import NameMixin
from testrail.models.mixins.fields.description import DescriptionMixin
from testrail.models.mixins.fields.assignedto_id import AssignedToIdMixin
from testrail.models.mixins.fields.case_ids import CaseIdsMixin
from testrail.models.mixins.fields.config_ids import ConfigIdsMixin
from testrail.models.mixins.fields.id import IdMixin
from testrail.models.mixins.fields.include_all import IncludeAllMixin
from testrail.models.mixins.fields.plan_id import PlanIdMixin
from testrail.models.mixins.fields.runs import RunsMixin

from testrail.models.mixins.methods.add import AddMixin
from testrail.models.mixins.methods.update import UpdateMixin
from testrail.models.mixins.methods.delete import DeleteMixin


class EntryModel(SuiteIdMixin, NameMixin, DescriptionMixin, AssignedToIdMixin, CaseIdsMixin, ConfigIdsMixin, IdMixin,
                 IncludeAllMixin, RunsMixin, PlanIdMixin, DeleteMixin, UpdateMixin, AddMixin, PostModel):

    ENDPOINTS = {
        'add': 'add_plan_entry/{plan_id}',
        'update': 'update_plan_entry/{plan_id}/{entry_id}',
        'delete': 'delete_plan_entry/{plan_id}/{entry_id}',
    }

    POST_FIELDS = {
        'add': [
            'suite_id',
            'name',
            'description',
            'assigned_to_id',
            'include_all',
            'case_ids',
            'config_ids',
            'runs'
        ],
        'update': [
            'name',
            'description',
            'assigned_to_id',
            'include_all',
            'case_ids'
        ]
    }

    SCHEMA = Schema({
        'id': str,
        'name': str,
        'runs': Or(list, None),
        'suite_id': int
    })

    def add(self, plan_id):
        response = self._add(plan_id=plan_id)
        self._update_data(response)

    def update(self):
        response = self._update(plan_id=self.plan_id, entry_id=self.id)
        self._update_data(response)

    def delete(self):
        self._delete(plan_id=self.plan_id, entry_id=self.id)
