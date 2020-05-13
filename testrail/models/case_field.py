from schema import Schema, Optional, Or

from testrail.models.base import PostModel
from testrail.models.mixins.fields import (CaseConfigsMixin, DescriptionMixin, DisplayOrderMixin, IdMixin,
                                           IncludeAllMixin, IsActiveMixin, LabelMixin, NameMixin, SystemNameMixin,
                                           TemplateIdMixin, TypeIdMixin)
from testrail.models.mixins.methods import AddMixin


class CaseFieldModel(CaseConfigsMixin, DescriptionMixin, DisplayOrderMixin, IdMixin, IncludeAllMixin, IsActiveMixin,
                     LabelMixin, NameMixin, SystemNameMixin, TemplateIdMixin, TypeIdMixin, AddMixin, PostModel):

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
        'configs': list,
        'description': Or(str, None),
        'display_order': int,
        'id': int,
        'label': Or(str, None),
        'name': str,
        'system_name': str,
        'type_id': int,
        Optional('include_all'): bool,
        Optional('is_active'): bool,
        Optional('template_ids'): list
    })

    def add(self):
        response = self._add()
        return response
