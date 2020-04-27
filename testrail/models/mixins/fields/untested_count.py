class UntestedCountMixin:
    @property
    def untested_count(self):
        return self._data.get('untested_count')
