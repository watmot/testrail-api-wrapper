class IsBaselineMixin:
    @property
    def is_baseline(self):
        return self._data.get('is_baseline')
