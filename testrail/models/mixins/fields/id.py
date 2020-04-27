class IdMixin:
    @property
    def id(self):
        return self._data.get('id')
