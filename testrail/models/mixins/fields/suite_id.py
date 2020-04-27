class SuiteIdMixin:
    @property
    def suite_id(self):
        return self._data.get('suite_id')

    @suite_id.setter
    def suite_id(self, arg):
        self._data['suite_id'] = arg
