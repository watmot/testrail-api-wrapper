class CustomStatus7CountMixin:
    @property
    def custom_status7_count(self):
        return self._data.get('custom_status7_count')
