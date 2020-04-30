from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods.get import GetMixin
from testrail.models.run import RunModel


class RunCollection(GetMixin, BaseCollection):
    MODEL = RunModel
    ENDPOINTS = {
        'get': 'get_runs/{project_id}'
    }

    def get(self, project_id=None, **parameters):
        query_string = self._parse_query_string(**parameters)
        response = self._get(project_id=project_id, query_string=query_string)
        return response



