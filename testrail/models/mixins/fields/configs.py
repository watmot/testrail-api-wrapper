class ConfigsMixin:
    @property
    def configs(self):
        return self._data.get('configs')
