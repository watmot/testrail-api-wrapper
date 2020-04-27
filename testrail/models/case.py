from schema import Schema, Or

from testrail.models.base import PostModel

from testrail.models.mixins.fields.created_by import CreatedByMixin
from testrail.models.mixins.fields.created_on import CreatedOnMixin
from testrail.models.mixins.fields.estimate import EstimateMixin
from testrail.models.mixins.fields.estimate_forecast import EstimateForecastMixin
from testrail.models.mixins.fields.id import IdMixin
from testrail.models.mixins.fields.milestone_id import MilestoneIdMixin
from testrail.models.mixins.fields.project_id import ProjectIdMixin
from testrail.models.mixins.fields.priority_id import PriorityIdMixin
from testrail.models.mixins.fields.refs import RefsMixin
from testrail.models.mixins.fields.section_id import SectionIdMixin
from testrail.models.mixins.fields.suite_id import SuiteIdMixin
from testrail.models.mixins.fields.template_id import TemplateIdMixin
from testrail.models.mixins.fields.title import TitleMixin
from testrail.models.mixins.fields.type_id import TypeIdMixin
from testrail.models.mixins.fields.updated_by import UpdatedByMixin
from testrail.models.mixins.fields.updated_on import UpdatedOnMixin

from testrail.models.mixins.methods.get import GetMixin
from testrail.models.mixins.methods.add import AddMixin
from testrail.models.mixins.methods.update import UpdateMixin
from testrail.models.mixins.methods.delete import DeleteMixin


class CaseModel(CreatedByMixin, CreatedOnMixin, EstimateMixin, EstimateForecastMixin, IdMixin, MilestoneIdMixin,
                ProjectIdMixin, PriorityIdMixin, RefsMixin, SectionIdMixin, SuiteIdMixin, TemplateIdMixin, TitleMixin,
                TypeIdMixin, UpdatedByMixin, UpdatedOnMixin,  DeleteMixin, UpdateMixin, AddMixin, GetMixin, PostModel):

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
        'updated_id': int,
        'updated_on': int
    })

    def get(self, case_id):
        response = self._get(case_id=case_id)
        self._update_data(response)

    def add(self, section_id):
        response = self._add(section_id=section_id)
        self._update_data(response)

    def update(self):
        response = self._update(case_id=self.id)
        self._update_data(response)

    def delete(self):
        self._delete(case_id=self.id)
