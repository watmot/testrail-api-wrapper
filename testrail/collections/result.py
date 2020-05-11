from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.result import ResultModel


class ResultCollection(GetMixin, BaseCollection):
    MODEL = ResultModel
    ENDPOINTS = {
        'get': 'get_results/{test_id}',
        'get_case': 'get_results_for_case/{run_id}/{case_id}',
        'get_run': 'get_results_for_case/{run_id}',
        'add': 'add_results/{run_id}',
        'add_cases': 'add_results_for_cases/{run_id}'
    }

    def get(self, test_id=None, **query_params):
        response = self._get(test_id=test_id, query_string_dict=query_params)
        return response

    def get_by_case_id(self, run_id=None, case_id=None, **query_params):
        response = self._get(endpoint_key='get_case', run_id=run_id, case_id=case_id, query_string_dict=query_params)
        return response

    def get_by_run_id(self, run_id=None, **parameters):
        response = self._get(endpoint_key='get_run', run_id=run_id, **parameters)
        return response

    def add(self, run_id):
        response = self._add(run_id=run_id)
        return response

    def add_for_cases(self, run_id):
        response = self._add(endpoint_key='add_cases', run_id=run_id)
        return response



