from schema import Schema, Optional, Or, Regex

from testrail.models.base import BaseModel
from testrail.models.mixins.fields import (AssignedToIdMixin, CaseIdMixin, CustomDescriptionMixin,
                                           CustomPreconditionMixin, CustomStepsMixin, CustomStepsSeparatedMixin,
                                           EstimateMixin, EstimateForecastMixin, IdMixin, MilestoneIdMixin,
                                           PriorityIdMixin, RefsMixin, RunIdMixin,StatusIdMixin, TitleMixin,
                                           TypeIdMixin)
from testrail.models.mixins.methods import GetMixin


class TestModel(AssignedToIdMixin, CaseIdMixin, CustomDescriptionMixin, CustomPreconditionMixin, CustomStepsMixin,
                CustomStepsSeparatedMixin, EstimateMixin, EstimateForecastMixin, IdMixin, MilestoneIdMixin,
                PriorityIdMixin, RefsMixin, RunIdMixin,StatusIdMixin, TitleMixin, TypeIdMixin, GetMixin, BaseModel):
    ENDPOINTS = {
        'get': 'get_test/{test_id}',
    }

    SCHEMA = Schema({
        'assignedto_id': Or(int, None),
        'case_id': int,
        'estimate': Or(str, None),
        'estimate_forecast': Or(str, None),
        'id': int,
        'milestone_id': Or(int, None),
        'priority_id': int,
        'refs': str,
        'run_id': int,
        'status_id': int,
        'title': str,
        'type_id': int,
        Optional(Regex(r'^custom_')): object
    })

    def get(self, test_id):
        response = self._get(test_id=test_id)
        return response
