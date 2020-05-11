from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.status import StatusModel


class StatusCollection(GetMixin, BaseCollection):
    MODEL = StatusModel
    ENDPOINTS = {
        'get': 'get_statuses'
    }

    def get(self, **query_params):
        response = self._get(query_string_dict=query_params)
        return response
