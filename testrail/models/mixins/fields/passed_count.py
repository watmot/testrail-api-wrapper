class PassedCountMixin:
    @property
    def passed_count(self):
        return self._data.get('passed_count')
