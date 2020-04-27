class CustomStatus1CountMixin:
    @property
    def custom_status1_count(self):
        return self._data.get('custom_status1_count')
