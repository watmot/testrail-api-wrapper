class TitleMixin:
    @property
    def title(self):
        return self._data.get('title')

    @title.setter
    def title(self, arg):
        self._data['title'] = str(arg)
