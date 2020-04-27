class VersionMixin:
    @property
    def version(self):
        return self._data.get('version')

    @version.setter
    def version(self, arg):
        self._data['version'] = str(arg)
