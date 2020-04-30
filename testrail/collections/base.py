from schema import Schema

from collections.abc import MutableSequence


class BaseCollection(MutableSequence):
    MODEL = None
    ENDPOINTS = None

    def __init__(self, **parameters):
        self._data = []

    def _check_item(self, item):
        return Schema(self.MODEL).is_valid(item)

    def __setitem__(self, index, value):
        if self._check_item(value):
            self._data.insert(index, value)
        else:
            raise TypeError()

    def __getitem__(self, index):
        return self._data[index]

    def __delitem__(self, index):
        del self._data[index]

    def __len__(self):
        return len(self._data)

    def insert(self, index, value):
        self._data.insert(index, value)
