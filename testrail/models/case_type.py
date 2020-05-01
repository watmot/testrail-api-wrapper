from schema import Schema

from testrail.models.base import PostModel

from testrail.models.mixins.fields.id import IdMixin
from testrail.models.mixins.fields.is_default import IsDefaultMixin
from testrail.models.mixins.fields.name import NameMixin


class CaseTypeModel(IdMixin, IsDefaultMixin, NameMixin, PostModel):

    SCHEMA = Schema({
        'id': int,
        'is_default': bool,
        'name': str
    })