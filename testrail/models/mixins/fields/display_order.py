class DisplayOrderMixin:
    @property
    def display_order(self):
        return self._data.get('display_order')
