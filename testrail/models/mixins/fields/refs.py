class RefsMixin:
    @property
    def refs(self):
        return self._data.get('refs')

    @refs.setter
    def refs(self, *args):
        arg = ' ,'.join(list(args))
        self._data['refs'] = arg
