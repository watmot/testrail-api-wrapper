class ParentIdMixin:
    @property
    def parent_id(self):
        return self._data.get('parent_id')
