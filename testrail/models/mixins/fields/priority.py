class PriorityMixin:
    @property
    def priority(self):
        return self._data.get('priority')
