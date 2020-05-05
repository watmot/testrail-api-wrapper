from schema import Schema

from testrail.models.base import BaseModel

from testrail.models.mixins.fields import IdMixin
from testrail.models.mixins.fields import IsDefaultMixin
from testrail.models.mixins.fields import NameMixin
from testrail.models.mixins.fields import PriorityMixin
from testrail.models.mixins.fields import ShortNameMixin


class PriorityModel(IdMixin, IsDefaultMixin, NameMixin, PriorityMixin, ShortNameMixin, BaseModel):
    SCHEMA = Schema({
        'id': int,
        'is_default': bool,
        'name': str,
        'priority': int,
        'short_name': str
    })
