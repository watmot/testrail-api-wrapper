class CustomStatus3CountMixin:
    @property
    def custom_status3_count(self):
        return self._data.get('custom_status3_count')
