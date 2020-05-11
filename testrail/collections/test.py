from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.test import TestModel


class TestCollection(BaseCollection):
    MODEL = TestModel
    ENDPOINTS = {
        'get': 'get_tests/{run_id}'
    }

    def get(self, run_id, **query_params):
        response = self._get(run_id=run_id, query_string_dict=query_params)
        return response

