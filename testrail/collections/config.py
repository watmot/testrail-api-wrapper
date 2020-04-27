from testrail.collections.base import BaseCollection
from testrail.models.config import ConfigModel


class ProjectCollection(BaseCollection):
    MODEL = ConfigModel

