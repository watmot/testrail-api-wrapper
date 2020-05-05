from schema import Schema, Or

from testrail.models.base import BaseModel

from testrail.models.mixins.fields import ConfigsMixin
from testrail.models.mixins.fields import DescriptionMixin
from testrail.models.mixins.fields import DisplayOrderMixin
from testrail.models.mixins.fields import IdMixin
from testrail.models.mixins.fields import LabelMixin
from testrail.models.mixins.fields import NameMixin
from testrail.models.mixins.fields import SystemNameMixin
from testrail.models.mixins.fields import TypeIdMixin


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
