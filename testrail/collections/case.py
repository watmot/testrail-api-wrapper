from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods.get import GetMixin
from testrail.models.case import CaseModel


class CaseCollection(GetMixin, BaseCollection):
    MODEL = CaseModel
    ENDPOINTS = {
        'get': 'get_cases/{project_id}'
    }
