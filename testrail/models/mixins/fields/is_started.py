class IsStartedMixin:
    @property
    def is_started(self):
        return self._data.get('is_started')

    @is_started.setter
    def is_started(self, arg):
        self._data['is_started'] = True if bool(arg) else False
