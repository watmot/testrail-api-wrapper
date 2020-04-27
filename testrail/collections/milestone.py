from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods.get import GetMixin
from testrail.models.milestone import MilestoneModel


class MilestoneCollection(GetMixin, BaseCollection):
    MODEL = MilestoneModel
    ENDPOINTS = {
        'get': 'get_milestones/{project_id}'
    }
