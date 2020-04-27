class StatusIdMixin:
    @property
    def status_id(self):
        return self._data.get('status_id')

    @status_id.setter
    def status_id(self, arg):
        self._data['status_id'] = arg
