from testrail.collections.base import BaseCollection
from testrail.models.test import TestModel


class TestCollection(BaseCollection):
    def __init__(self, data=None, **kwargs):
        super().__init__(data=data, model=TestModel, **kwargs)
