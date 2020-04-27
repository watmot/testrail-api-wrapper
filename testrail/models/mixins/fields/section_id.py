class SectionIdMixin:
    @property
    def section_id(self):
        return self._data.get('section_id')

    @section_id.setter
    def section_id(self, arg):
        self._data['section_id'] = arg
