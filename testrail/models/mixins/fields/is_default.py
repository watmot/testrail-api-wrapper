class IsDefaultMixin:
    @property
    def is_default(self):
        return self._data.get('is_default')
