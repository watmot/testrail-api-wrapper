from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.case_type import CaseTypeModel


class CaseTypeCollection(GetMixin, BaseCollection):
    MODEL = CaseTypeModel
    ENDPOINTS = {
        'get': 'get_case_types'
    }

    def get(self, **query_params):
        response = self._get(query_string_dict=query_params)
        return response

