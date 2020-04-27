class FailedCountMixin:
    @property
    def failed_count(self):
        return self._data.get('failed_count')
