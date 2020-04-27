class LabelMixin:
    @property
    def label(self):
        return self._data.get('label')
