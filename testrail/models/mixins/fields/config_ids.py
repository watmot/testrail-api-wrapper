class ConfigIdsMixin:
    @property
    def config_ids(self):
        return self._data.get('config_ids')

    @config_ids.setter
    def config_ids(self, arg):
        self._data['config_ids'] = arg
