from testrail.collections.base import BaseCollection
from testrail.models.config_group import ConfigGroupModel


class ConfigGroupCollection(BaseCollection):
    MODEL = ConfigGroupModel
