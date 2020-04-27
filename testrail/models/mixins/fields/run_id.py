class RunIdMixin:
    @property
    def run_id(self):
        return self._data.get('run_id')
