from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.report import ReportModel


class ReportCollection(GetMixin, BaseCollection):
    MODEL = ReportModel
    ENDPOINTS = {
        'get': 'get_reports/{project_id}'
    }

    def get(self, project_id, **query_params):
        response = self._get(project_id=project_id, query_string_dict=query_params)
        return response
