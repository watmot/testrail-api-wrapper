from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.result import ResultModel


class ResultCollection(GetMixin, BaseCollection):
    MODEL = ResultModel
    ENDPOINTS = {
        'get': 'get_results/{test_id}{query_string}'
    }

    def get(self, test_id, **parameters):
        query_string = self._parse_query_string(**parameters)
        response = self._get(test_id=test_id, query_string=query_string)
        return response
