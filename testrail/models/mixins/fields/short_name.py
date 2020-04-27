class ShortNameMixin:
    @property
    def short_name(self):
        return self._data.get('short_name')
