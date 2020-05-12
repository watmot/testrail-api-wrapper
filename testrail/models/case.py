from schema import Schema, Optional, Or, Regex

from testrail.models.base import PostModel

from testrail.models.mixins.fields import CreatedByMixin
from testrail.models.mixins.fields import CreatedOnMixin
from testrail.models.mixins.fields import DisplayOrderMixin
from testrail.models.mixins.fields import EstimateMixin
from testrail.models.mixins.fields import EstimateForecastMixin
from testrail.models.mixins.fields import IdMixin
from testrail.models.mixins.fields import MilestoneIdMixin
from testrail.models.mixins.fields import PriorityIdMixin
from testrail.models.mixins.fields import RefsMixin
from testrail.models.mixins.fields import SectionIdMixin
from testrail.models.mixins.fields import SuiteIdMixin
from testrail.models.mixins.fields import TemplateIdMixin
from testrail.models.mixins.fields import TitleMixin
from testrail.models.mixins.fields import TypeIdMixin
from testrail.models.mixins.fields import UpdatedByMixin
from testrail.models.mixins.fields import UpdatedOnMixin

from testrail.models.mixins.methods import GetMixin
from testrail.models.mixins.methods import AddMixin
from testrail.models.mixins.methods import UpdateMixin
from testrail.models.mixins.methods import DeleteMixin


class CaseModel(CreatedByMixin, CreatedOnMixin, DisplayOrderMixin, EstimateMixin, EstimateForecastMixin, IdMixin,
                MilestoneIdMixin, PriorityIdMixin, RefsMixin, SectionIdMixin, SuiteIdMixin, TemplateIdMixin, TitleMixin,
                TypeIdMixin, UpdatedByMixin, UpdatedOnMixin, DeleteMixin, UpdateMixin, AddMixin, GetMixin, PostModel):
    ENDPOINTS = {
        'get': 'get_case/{case_id}',
        'add': 'add_case/{section_id}',
        'update': 'update_case/{case_id}',
        'delete': 'delete_case/{case_id}',
    }

    POST_FIELDS = {
        'add': [
            'title',
            'template_id',
            'type_id',
            'priority_id',
            'estimate',
            'milestone_id',
            'refs'
        ],
        'update': [
            'title',
            'template_id',
            'type_id',
            'priority_id',
            'estimate',
            'milestone_id',
            'refs'
        ]
    }

    SCHEMA = Schema({
        'created_by': int,
        'created_on': int,
        'display_order': int,
        'estimate': Or(str, None),
        'estimate_forecast': Or(str, None),
        'id': int,
        'milestone_id': Or(int, None),
        'priority_id': Or(int, None),
        'refs': Or(str, None),
        'section_id': int,
        'suite_id': int,
        'template_id': int,
        'title': str,
        'type_id': int,
        'updated_by': int,
        'updated_on': int,
        Optional(Regex(r'^custom_')): object
    })

    def get(self, case_id):
        response = self._get(case_id=case_id)
        return response

    def add(self, section_id):
        response = self._add(section_id=section_id)
        return response

    def update(self):
        response = self._update(case_id=self.id)
        return response

    def delete(self):
        response = self._delete(case_id=self.id)
        return response
