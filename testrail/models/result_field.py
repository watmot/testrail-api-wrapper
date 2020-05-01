from schema import Schema, Or

from testrail.models.base import BaseModel

from testrail.models.mixins.fields.configs import ConfigsMixin
from testrail.models.mixins.fields.description import DescriptionMixin
from testrail.models.mixins.fields.display_order import DisplayOrderMixin
from testrail.models.mixins.fields.id import IdMixin
from testrail.models.mixins.fields.label import LabelMixin
from testrail.models.mixins.fields.name import NameMixin
from testrail.models.mixins.fields.system_name import SystemNameMixin
from testrail.models.mixins.fields.type_id import TypeIdMixin


class ResultFieldModel(ConfigsMixin, DescriptionMixin, DisplayOrderMixin, IdMixin, LabelMixin, NameMixin,
                       SystemNameMixin, TypeIdMixin, BaseModel):
    SCHEMA = Schema({
        'configs': list,
        'description': Or(str, None),
        'display_order': int,
        'id': int,
        'label': Or(str, None),
        'name': str,
        'system_name': str,
        'type_id': int
    })
