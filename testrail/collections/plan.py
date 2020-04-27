from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods.get import GetMixin
from testrail.models.plan import PlanModel


class PlanCollection(GetMixin, BaseCollection):
    MODEL = PlanModel
    ENDPOINTS = {
        'get': 'get_plans/{project_id}'
    }
