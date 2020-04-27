from testrail.collections.base import BaseCollection
from testrail.collections.mixins.methods.get import GetMixin
from testrail.models.section import SectionModel


class SectionCollection(GetMixin, BaseCollection):
    MODEL = SectionModel
    ENDPOINTS = {
        'get': 'get_sections/{project_id}'
    }
