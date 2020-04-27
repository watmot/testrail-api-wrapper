class EmailMixin:
    @property
    def email(self):
        return self._data.get('email')
