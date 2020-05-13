from schema import Schema

from testrail.models.base import BaseModel
from testrail.models.mixins.fields import IdMixin, IsDefaultMixin, NameMixin, PriorityMixin, ShortNameMixin


class PriorityModel(IdMixin, IsDefaultMixin, NameMixin, PriorityMixin, ShortNameMixin, BaseModel):
    SCHEMA = Schema({
        'id': int,
        'is_default': bool,
        'name': str,
        'priority': int,
        'short_name': str
    })
