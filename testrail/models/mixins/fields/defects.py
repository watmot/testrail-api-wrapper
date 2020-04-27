class DefectsMixin:
    @property
    def defects(self):
        return self._data.get('defects')

    @defects.setter
    def defects(self, *args):
        arg = ' ,'.join(list(args))
        self._data['defects'] = arg