from schema import Schema

from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods.get import GetMixin
from testrail.models.project import ProjectModel


class ProjectCollection(GetMixin, BaseCollection):
    MODEL = ProjectModel
    ENDPOINTS = {
        'get': 'get_projects'
    }