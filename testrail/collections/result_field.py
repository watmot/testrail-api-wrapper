from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.result_field import ResultFieldModel


class ResultFieldCollection(GetMixin, BaseCollection):
    MODEL = ResultFieldModel
    ENDPOINTS = {
        'get': 'get_result_fields{query_string}'
    }

    def get(self, **parameters):
        query_string = self._parse_query_string(**parameters)
        response = self._get(query_string=query_string)
        return response
