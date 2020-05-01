from schema import Schema

from testrail.models.base import BaseModel

from testrail.models.mixins.fields.color_bright import ColorBrightMixin
from testrail.models.mixins.fields.color_dark import ColorDarkMixin
from testrail.models.mixins.fields.color_medium import ColorMediumMixin
from testrail.models.mixins.fields.id import IdMixin
from testrail.models.mixins.fields.is_final import IsFinalMixin
from testrail.models.mixins.fields.is_system import IsSystemMixin
from testrail.models.mixins.fields.is_untested import IsUntestedMixin
from testrail.models.mixins.fields.label import LabelMixin
from testrail.models.mixins.fields.name import NameMixin


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
