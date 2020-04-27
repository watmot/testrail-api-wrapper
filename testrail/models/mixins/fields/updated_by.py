class UpdatedByMixin:
    @property
    def updated_by(self):
        return self._data.get('updated_by')
