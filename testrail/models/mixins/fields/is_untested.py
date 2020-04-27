class IsUntestedMixin:
    @property
    def is_untested(self):
        return self._data.get('is_untested')
