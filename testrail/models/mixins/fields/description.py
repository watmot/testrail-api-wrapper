class DescriptionMixin:
    @property
    def description(self):
        return self._data.get('description')

    @description.setter
    def description(self, arg):
        self._data['description'] = str(arg)
