class CaseIdMixin:
    @property
    def case_id(self):
        return self._data.get('case_id')
