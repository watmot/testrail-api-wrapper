class GroupIdMixin:
    @property
    def group_id(self):
        return self._data.get('group_id')
