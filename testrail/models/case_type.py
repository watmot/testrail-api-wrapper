from schema import Schema

from testrail.models.base import PostModel
from testrail.models.mixins.fields import IdMixin, IsDefaultMixin, NameMixin


class CaseTypeModel(IdMixin, IsDefaultMixin, NameMixin, PostModel):

    SCHEMA = Schema({
        'id': int,
        'is_default': bool,
        'name': str
    })
