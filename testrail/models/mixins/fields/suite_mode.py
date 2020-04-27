class SuiteModeMixin:
    @property
    def suite_mode(self):
        return self._data.get('suite_mode')

    @suite_mode.setter
    def suite_mode(self, arg):
        modes = [1, 2, 3]
        if arg not in modes:
            raise ValueError('\'arg\' must be in {}'.format(modes))
        self._data['suite_mode'] = arg
