class UrlMixin:
    @property
    def url(self):
        return self._data.get('url')
