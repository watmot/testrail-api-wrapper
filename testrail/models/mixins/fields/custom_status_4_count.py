class CustomStatus4CountMixin:
    @property
    def custom_status4_count(self):
        return self._data.get('custom_status4_count')
