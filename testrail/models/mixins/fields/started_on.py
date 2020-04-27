class StartedOnMixin:
    @property
    def started_on(self):
        return self._data.get('started_on')
