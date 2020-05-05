from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.section import SectionModel


class SectionCollection(GetMixin, BaseCollection):
    MODEL = SectionModel
    ENDPOINTS = {
        'get': 'get_sections/{project_id}{query_string}'
    }

    def get(self, project_id, **parameters):
        query_string = self._parse_query_string(**parameters)
        response = self._get(project_id=project_id, query_string=query_string)
        return response
