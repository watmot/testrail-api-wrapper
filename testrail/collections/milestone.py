from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.milestone import MilestoneModel


class MilestoneCollection(GetMixin, BaseCollection):
    MODEL = MilestoneModel
    ENDPOINTS = {
        'get': 'get_milestones/{project_id}{query_string}'
    }

    def get(self, project_id, **parameters):
        query_string = self._parse_query_string(**parameters)
        response = self._get(project_id=project_id, query_string=query_string)
        return response
