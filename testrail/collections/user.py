from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.user import UserModel


class UserCollection(GetMixin, BaseCollection):
    MODEL = UserModel
    ENDPOINTS = {
        'get': 'get_users'
    }

    def get(self, **query_params):
        response = self._get(endpoint_key='get', query_string_dict=query_params)
        return response
