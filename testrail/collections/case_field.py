from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.case_field import CaseFieldModel


class CaseFieldCollection(GetMixin, BaseCollection):
    MODEL = CaseFieldModel
    ENDPOINTS = {
        'get': 'get_case_fields'
    }

    def get(self, **query_params):
        response = self._get(query_string_dict=query_params)
        return response
