class MilestoneIdMixin:
    @property
    def milestone_id(self):
        return self._data.get('milestone_id')
