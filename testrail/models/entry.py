from schema import Schema, Or

from testrail.models.base import PostModel
from testrail.models.plan import PlanModel
from testrail.models.mixins.fields import (SuiteIdMixin, NameMixin, DescriptionMixin, AssignedToIdMixin, CaseIdsMixin,
                                           ConfigIdsMixin, IdMixin, IncludeAllMixin, PlanIdMixin, RunsMixin)
from testrail.models.mixins.methods import AddMixin, UpdateMixin, DeleteMixin


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
        'description': Or(str, None),
        'assigned_to_id': Or(int, None),
        'include_all': bool,
        'case_ids': list,
        'config_ids': list,
        'runs': list,
        'suite_id': int
    })

    def get(self, plan_id, entry_id):
        plan = PlanModel()
        plan.get(plan_id=plan_id)
        for entry in plan.entries:
            if entry['id'] == entry_id:
                self._update_data(entry)
        else:
            raise KeyError

    def add(self, plan_id):
        response = self._add(plan_id=plan_id)
        return response

    def update(self):
        response = self._update(plan_id=self.plan_id, entry_id=self.id)
        return response

    def delete(self):
        response = self._delete(plan_id=self.plan_id, entry_id=self.id)
        return response
