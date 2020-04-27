class CreatedByMixin:
    @property
    def created_by(self):
        return self._data.get('created_by')
