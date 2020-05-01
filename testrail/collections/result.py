from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods.get import GetMixin
from testrail.models.result import ResultModel


class ResultCollection(GetMixin, BaseCollection):
    MODEL = ResultModel
    ENDPOINTS = {
        'get': 'get_results/{project_id}{query_string}'
    }