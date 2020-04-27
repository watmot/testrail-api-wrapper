class CustomStatus5CountMixin:
    @property
    def custom_status5_count(self):
        return self._data.get('custom_status5_count')
