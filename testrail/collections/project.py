from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.project import ProjectModel


class ProjectCollection(GetMixin, BaseCollection):
    MODEL = ProjectModel
    ENDPOINTS = {
        'get': 'get_projects'
    }

    def get(self, **query_params):
        response = self._get(query_string_dict=query_params)
        return response
