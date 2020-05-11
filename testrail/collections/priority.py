from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.priority import PriorityModel


class PriorityCollection(GetMixin, BaseCollection):
    MODEL = PriorityModel
    ENDPOINTS = {
        'get': 'get_priorities'
    }

    def get(self, **query_params):
        response = self._get(query_string_dict=query_params)
