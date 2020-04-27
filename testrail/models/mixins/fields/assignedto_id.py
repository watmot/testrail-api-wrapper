class AssignedToIdMixin:
    @property
    def assignedto_id(self):
        return self._data.get('assigned_to_id')

    @assignedto_id.setter
    def assignedto_id(self, arg):
        self._data['assigned_to_id'] = int(arg)