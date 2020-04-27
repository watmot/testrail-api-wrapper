class TestIdMixin:
    @property
    def test_id(self):
        return self._data.get('test_id')
