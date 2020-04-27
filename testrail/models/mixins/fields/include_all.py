class IncludeAllMixin:
    @property
    def include_all(self):
        return self._data.get('include_all')

    @include_all.setter
    def include_all(self, arg):
        self._data['include_all'] = True if bool(arg) else False
