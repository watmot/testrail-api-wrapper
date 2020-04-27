class IsFinalMixin:
    @property
    def is_final(self):
        return self._data.get('is_final')
