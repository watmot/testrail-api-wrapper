class CustomStatus6CountMixin:
    @property
    def custom_status6_count(self):
        return self._data.get('custom_status6_count')
