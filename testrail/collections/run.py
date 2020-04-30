from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods.get import GetMixin
from testrail.models.run import RunModel


class RunCollection(GetMixin, BaseCollection):
    MODEL = RunModel
    ENDPOINTS = {
        'get': 'get_runs/{test_id}'
    }
