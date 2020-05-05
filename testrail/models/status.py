from schema import Schema

from testrail.models.base import BaseModel

from testrail.models.mixins.fields import ColorBrightMixin
from testrail.models.mixins.fields import ColorDarkMixin
from testrail.models.mixins.fields import ColorMediumMixin
from testrail.models.mixins.fields import IdMixin
from testrail.models.mixins.fields import IsFinalMixin
from testrail.models.mixins.fields import IsSystemMixin
from testrail.models.mixins.fields import IsUntestedMixin
from testrail.models.mixins.fields import LabelMixin
from testrail.models.mixins.fields import NameMixin


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
