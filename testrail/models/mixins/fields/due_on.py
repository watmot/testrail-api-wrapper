class DueOnMixin:
    @property
    def due_on(self):
        return self._data.get('due_on')

    @due_on.setter
    def due_on(self, arg):
        self._data['due_on'] = int(arg)
