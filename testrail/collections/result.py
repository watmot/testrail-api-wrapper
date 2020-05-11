from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.result import ResultModel


class ResultCollection(GetMixin, BaseCollection):
    MODEL = ResultModel
    ENDPOINTS = {
        'get': 'get_results/{test_id}{query_string}',
        'get_case': 'get_results_for_case/{run_id}/{case_id}',
        'get_run': 'get_results_for_case/{run_id}',
        'add': 'add_results/{run_id}'
    }

    def get(self, test_id=None, run_id=None, case_id=None, **parameters):
        query_string = self._parse_query_string(**parameters)
        if test_id:
            response = self._get(test_id=test_id, query_string=query_string)
            return response
        if run_id and case_id:
            response = self._get(endpoint_key='get_case', run_id=run_id, case_id=case_id, query_string=query_string)
            return response
        if run_id:
            response = self._get(endpoint_key='get_run', run_id=run_id, **parameters)
            return response
        raise Exception

    def add(self, run_id):
        response = self._add(run_id=run_id)
        return response


