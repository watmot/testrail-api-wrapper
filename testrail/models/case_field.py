from schema import Schema, Optional, Or

from testrail.models.base import PostModel

from testrail.models.mixins.fields import DescriptionMixin
from testrail.models.mixins.fields import DisplayOrderMixin
from testrail.models.mixins.fields import IdMixin
from testrail.models.mixins.fields import LabelMixin
from testrail.models.mixins.fields import NameMixin
from testrail.models.mixins.fields import SystemNameMixin
from testrail.models.mixins.fields import TypeIdMixin

from testrail.models.mixins.methods import AddMixin


class CaseFieldModel(DescriptionMixin, DisplayOrderMixin, IdMixin, LabelMixin, NameMixin, SystemNameMixin, TypeIdMixin,
                     AddMixin, PostModel):

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
        Optional('entity_id'): int,
        'id': int,
        'label': Or(str, None),
        Optional('location_id'): int,
        'name': str,
        Optional('is_multi'): int,
        Optional('is_active'): int,
        Optional('status_id'): int,
        Optional('is_system'): int,
        Optional('include_all'): int,
        'system_name': str,
        'type_id': int,
        Optional('template_ids'): list
    })

    def add(self):
        response = self._add()
        return response
