class NameMixin:
    @property
    def name(self):
        return self._data.get('name')

    @name.setter
    def name(self, arg):
        self._data['name'] = arg
