from schema import Schema

from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods.get import GetMixin
from testrail.models.case import CaseModel


class CaseCollection(GetMixin, BaseCollection):
    MODEL = CaseModel
    ENDPOINTS = {
        'get': 'get_cases/{project_id}'
    }

    def get(self, project_id, **parameters):
        query_string = self._parse_query_string(**parameters)
        response = self._get(project_id=project_id, query_string=query_string)
        return response