class ElapsedMixin:
    @property
    def elapsed(self):
        return self._data.get('elapsed')

    @elapsed.setter
    def elapsed(self, arg):
        # TODO Add logic to handle timespan type
        self._data['elapsed'] = str(arg)
