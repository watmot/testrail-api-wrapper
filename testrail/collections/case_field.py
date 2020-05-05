from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.case_field import CaseFieldModel


class CaseFieldCollection(GetMixin, BaseCollection):
    MODEL = CaseFieldModel
    ENDPOINTS = {
        'get': 'get_case_fields{query_string}'
    }

    def get(self, **parameters):
        query_string = self._parse_query_string(**parameters)
        response = self._get(query_string=query_string)
        return response
