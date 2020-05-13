from schema import Schema, Or

from testrail.models.base import BaseModel

from testrail.models.mixins.fields import (ConfigsMixin, DescriptionMixin, DisplayOrderMixin, IdMixin, LabelMixin, \
                                           NameMixin, SystemNameMixin, TypeIdMixin)


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
