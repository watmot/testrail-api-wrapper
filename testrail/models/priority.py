from schema import Schema

from testrail.models.base import BaseModel

from testrail.models.mixins.fields.id import IdMixin
from testrail.models.mixins.fields.is_default import IsDefaultMixin
from testrail.models.mixins.fields.name import NameMixin
from testrail.models.mixins.fields.priority import PriorityMixin
from testrail.models.mixins.fields.short_name import ShortNameMixin


class PriorityModel(IdMixin, IsDefaultMixin, NameMixin, PriorityMixin, ShortNameMixin, BaseModel):
    SCHEMA = Schema({
        'id': int,
        'is_default': bool,
        'name': str,
        'priority': int,
        'short_name': str
    })
