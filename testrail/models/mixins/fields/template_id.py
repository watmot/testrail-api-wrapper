class TemplateIdMixin:
    @property
    def template_id(self):
        return self._data.get('template_id')

    @template_id.setter
    def template_id(self, arg):
        self._data['title'] = int(arg)
