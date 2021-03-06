from schema import Schema

from testrail.models.base import BaseModel
from testrail.models.mixins.fields import EmailMixin, IdMixin, IsActiveMixin, NameMixin
from testrail.models.mixins.methods import GetMixin


class UserModel(EmailMixin, IdMixin, IsActiveMixin, NameMixin, GetMixin, BaseModel):
    ENDPOINTS = {
        'get': 'get_user/{user_id}',
        'get_email': 'get_user_by_email&email={email}'
    }

    SCHEMA = Schema({
        'email': str,
        'id': int,
        'is_active': bool,
        'name': str,
    })

    def get(self, user_id=None):
        response = self._get(user_id=user_id)
        return response

    def get_by_email(self, email=None):
        response = self._get(endpoint_key='get_email', email=email)
        return response
