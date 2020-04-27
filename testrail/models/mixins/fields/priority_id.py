class PriorityIdMixin:
    @property
    def priority_id(self):
        return self._data.get('priority_id')
