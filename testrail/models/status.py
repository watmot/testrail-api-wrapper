from schema import Schema

from testrail.models.base import BaseModel
from testrail.models.mixins.fields import (ColorBrightMixin, ColorDarkMixin, ColorMediumMixin, IdMixin, IsFinalMixin,
                                           IsSystemMixin, IsUntestedMixin, LabelMixin, NameMixin)


class StatusModel(ColorBrightMixin, ColorDarkMixin, ColorMediumMixin, IdMixin, IsFinalMixin, IsSystemMixin,
                  IsUntestedMixin, LabelMixin, NameMixin, BaseModel):
    SCHEMA = Schema({
        'color_bright': int,
        'color_dark': int,
        'color_medium': int,
        'id': int,
        'is_final': bool,
        'is_system': bool,
        'is_untested': bool,
        'label': str,
        'name': str
    })
