from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.plan import PlanModel


class PlanCollection(GetMixin, BaseCollection):
    MODEL = PlanModel
    ENDPOINTS = {
        'get': 'get_plans/{project_id}'
    }

    def get(self, project_id, **query_params):
        response = self._get(project_id=project_id, query_string_dict=query_params)
        return response
