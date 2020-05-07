from schema import Schema

from testrail.models.base import BaseModel

from testrail.models.mixins.fields import EmailMixin
from testrail.models.mixins.fields import IdMixin
from testrail.models.mixins.fields import IsActiveMixin
from testrail.models.mixins.fields import NameMixin

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

    def get(self, user_id=None, email=None):
        if user_id:
            response = self._get(user_id=user_id)
            return response
        if email:
            response = self._get(endpoint_key='get_email', email=email)
            return response
        raise Exception
