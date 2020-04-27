class ConfigMixin:
    @property
    def config(self):
        return self._data.get('config')




