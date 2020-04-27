class PlatformMixin:
    @property
    def platform(self):
        return self._data.get('platform')

    @platform.setter
    def platform(self, arg):
        self._data['platform'] = str(arg)