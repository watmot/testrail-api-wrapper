class IsActiveMixin:
    @property
    def is_active(self):
        return self._data.get('is_active')
