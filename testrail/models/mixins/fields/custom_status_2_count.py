class CustomStatus2CountMixin:
    @property
    def custom_status2_count(self):
        return self._data.get('custom_status2_count')
