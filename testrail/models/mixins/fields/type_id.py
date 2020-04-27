class TypeIdMixin:
    @property
    def type_id(self):
        return self._data.get('type_id')

    @type_id.setter
    def type_id(self, arg):
        self._data['type_id'] = int(arg)
