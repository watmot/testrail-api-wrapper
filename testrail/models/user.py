from schema import Schema

from testrail.models.base import BaseModel

from testrail.models.mixins.fields.email import EmailMixin
from testrail.models.mixins.fields.id import IdMixin
from testrail.models.mixins.fields.is_active import IsActiveMixin
from testrail.models.mixins.fields.name import NameMixin

from testrail.models.mixins.methods.get import GetMixin


class UserModel(EmailMixin, IdMixin, IsActiveMixin, NameMixin, GetMixin, BaseModel):
    ENDPOINTS = {
        'get': 'get_user/{user_id}'
    }

    SCHEMA = Schema({
        'email': str,
        'id': int,
        'is_active': bool,
        'name': str,
    })

    def get(self, user_id):
        response = self._get(user_id=user_id)
        return response
