from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods.get import GetMixin
from testrail.models.template import TemplateModel


class TemplateCollection(GetMixin, BaseCollection):
    MODEL = TemplateModel
    ENDPOINTS = {
        'get': 'get_templates/{project_id}{query_string}'
    }

    def get(self, project_id=None, **parameters):
        query_string = self._parse_query_string(**parameters)
        response = self._get(project_id=project_id, query_string=query_string)
        return response