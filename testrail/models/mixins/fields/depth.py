class DepthMixin:
    @property
    def depth(self):
        return self._data.get('depth')
