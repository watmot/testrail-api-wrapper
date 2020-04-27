from testrail.models.base import BaseModel

from testrail.models.mixins.fields.assignedto_id import AssignedToIdMixin
from testrail.models.mixins.fields.case_id import CaseIdMixin
from testrail.models.mixins.fields.estimate import EstimateMixin
from testrail.models.mixins.fields.estimate_forecast import EstimateForecastMixin
from testrail.models.mixins.fields.id import IdMixin
from testrail.models.mixins.fields.milestone_id import MilestoneIdMixin
from testrail.models.mixins.fields.priority_id import PriorityIdMixin
from testrail.models.mixins.fields.refs import RefsMixin
from testrail.models.mixins.fields.run_id import RunIdMixin
from testrail.models.mixins.fields.status_id import StatusIdMixin
from testrail.models.mixins.fields.title import TitleMixin
from testrail.models.mixins.fields.type_id import TypeIdMixin

from testrail.models.mixins.methods.get import GetMixin


class TestModel(AssignedToIdMixin, CaseIdMixin, EstimateMixin, EstimateForecastMixin, IdMixin, MilestoneIdMixin,
                PriorityIdMixin, RefsMixin, RunIdMixin, StatusIdMixin, TitleMixin, TypeIdMixin, GetMixin, BaseModel):

    ENDPOINTS = {
        'get': 'get_test/{test_id}',
        'get_collection': 'get_tests/{run_id}{params}',
    }
