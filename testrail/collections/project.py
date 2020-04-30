from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods.get import GetMixin
from testrail.models.project import ProjectModel


class ProjectCollection(GetMixin, BaseCollection):
    MODEL = ProjectModel
    ENDPOINTS = {
        'get': 'get_projects'
    }

    def get(self, **parameters):
        query_string = self._parse_query_string(**parameters)
        response = self._get(query_string=query_string)
        return response
