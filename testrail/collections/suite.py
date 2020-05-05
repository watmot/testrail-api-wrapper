from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.suite import SuiteModel


class SuiteCollection(GetMixin, BaseCollection):
    MODEL = SuiteModel
    ENDPOINTS = {
        'get': 'get_suites/{project_id}{query_string}'
    }

    def get(self, project_id=None, **parameters):
        query_string = self._parse_query_string(**parameters)
        response = self._get(project_id=project_id, query_string=query_string)
        return response
