from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.test import TestModel


class TestCollection(BaseCollection):
    MODEL = TestModel
    ENDPOINTS = {
        'get': 'get_tests/{run_id}{query_string}'
    }

    def get(self, run_id, **parameters):
        query_string = self._parse_query_string(**parameters)
        response = self._get(run_id=run_id, query_string=query_string)
        return response

