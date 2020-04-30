from schema import Schema, Optional, Or

from testrail.models.base import PostModel

from testrail.models.mixins.fields.description import DescriptionMixin
from testrail.models.mixins.fields.display_order import DisplayOrderMixin
from testrail.models.mixins.fields.id import IdMixin
from testrail.models.mixins.fields.label import LabelMixin
from testrail.models.mixins.fields.name import NameMixin
from testrail.models.mixins.fields.system_name import SystemNameMixin
from testrail.models.mixins.fields.type_id import TypeIdMixin

from testrail.models.mixins.methods.add import AddMixin


class CaseFieldModel(DescriptionMixin, DisplayOrderMixin, IdMixin, LabelMixin, NameMixin, SystemNameMixin, TypeMixin,
                     TypeIdMixin, AddMixin, PostModel):

    ENDPOINTS = {
        'add': 'add_case_field/'
    }

    POST_FIELDS = {
        'add': [
            'type',
            'name',
            'label',
            'description',
            'include_all',
            'template_ids',
            'configs'
        ]
    }

    SCHEMA = Schema({
        'type': int,
        'created_on': int,
        'custom_description': Or(str, None),
        'custom_precondition': Or(str, None),
        'custom_steps': Or(str, None),
        Optional('custom_steps_separated', default=[]): list,
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
        'updated_on': int
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

#  TODO ConfigsMixin
