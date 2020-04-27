class CaseIdsMixin:
    @property
    def case_ids(self):
        return self._data.get('case_ids')

    @case_ids.setter
    def case_ids(self, arg):
        ids = [case.id for case in arg]
        self._data['case_ids'] = ids
