class RetestCountMixin:
    @property
    def retest_count(self):
        return self._data.get('retest_count')
