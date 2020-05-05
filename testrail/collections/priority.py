from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.priority import PriorityModel


class PriorityCollection(GetMixin, BaseCollection):
    MODEL = PriorityModel
    ENDPOINTS = {
        'get': 'get_priorities{query_string}'
    }

    def get(self, **parameters):
        query_string = self._parse_query_string(**parameters)
        response = self._get(query_string=query_string)
        return response
