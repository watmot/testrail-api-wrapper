from schema import Schema

from testrail.models.base import BaseModel

from testrail.models.mixins.fields import IdMixin
from testrail.models.mixins.fields import IsDefaultMixin
from testrail.models.mixins.fields import NameMixin


class TemplateModel(IdMixin, IsDefaultMixin, NameMixin, BaseModel):
    SCHEMA = Schema({
        'id': int,
        'is_default': bool,
        'name': str,
    })
