from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods import GetMixin
from testrail.models.result_field import ResultFieldModel


class ResultFieldCollection(GetMixin, BaseCollection):
    MODEL = ResultFieldModel
    ENDPOINTS = {
        'get': 'get_result_fields'
    }

    def get(self, **query_params):
        response = self._get(query_string_dict=query_params)
        return response
