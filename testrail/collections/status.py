from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods.get import GetMixin
from testrail.models.status import StatusModel


class StatusCollection(GetMixin, BaseCollection):
    MODEL = StatusModel
    ENDPOINTS = {
        'get': 'get_statuses{query_string}'
    }

    def get(self, **parameters):
        query_string = self._parse_query_string(**parameters)
        response = self._get(query_string=query_string)
        return response
