from testrail.models.config import ConfigCollection


class ConfigsMixin:
    @property
    def configs(self):
        return self._data.get('configs')

    @configs.setter
    def configs(self, arg):
        response = arg['configs']
        self._data['configs'] = ConfigCollection(response=response)
