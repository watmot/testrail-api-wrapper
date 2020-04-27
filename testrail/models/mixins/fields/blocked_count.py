class BlockedCountMixin:
    @property
    def blocked_count(self):
        return self._data.get('blocked_count')
