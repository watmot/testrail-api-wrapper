class IsSystemMixin:
    @property
    def is_system(self):
        return self._data.get('is_system')
