from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.suite import SuiteModel


class SuiteCollection(GetMixin, BaseCollection):
    MODEL = SuiteModel
    ENDPOINTS = {
        'get': 'get_suites/{project_id}'
    }

    def get(self, project_id, **query_params):
        response = self._get(project_id=project_id, query_string_dict=query_params)
        return response
