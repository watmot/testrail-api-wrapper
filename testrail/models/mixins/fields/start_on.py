class StartOnMixin:
    @property
    def start_on(self):
        return self._data.get('start_on')

    @start_on.setter
    def start_on(self, arg):
        self._data['start_on'] = int(arg)