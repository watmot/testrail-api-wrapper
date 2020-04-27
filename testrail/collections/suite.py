from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods.get import GetMixin
from testrail.models.suite import SuiteModel


class SuiteCollection(GetMixin, BaseCollection):
    MODEL = SuiteModel
    ENDPOINTS = {
        'get': 'get_suites/{project_id}'
    }
