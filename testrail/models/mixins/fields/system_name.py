class SystemNameMixin:
    @property
    def system_name(self):
        return self._data.get('name')

    @system_name.setter
    def system_name(self, arg):
        self._data['name'] = arg
