class IsMasterMixin:
    @property
    def is_master(self):
        return self._data.get('is_master')
