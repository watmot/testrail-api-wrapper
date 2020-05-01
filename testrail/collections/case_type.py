from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods.get import GetMixin
from testrail.models.case_type import CaseTypeModel


class CaseTypeCollection(GetMixin, BaseCollection):
    MODEL = CaseTypeModel
    ENDPOINTS = {
        'get': 'get_case_types{query_string}'
    }

    def get(self, **parameters):
        query_string = self._parse_query_string(**parameters)
        response = self._get(query_string=query_string)
        return response

