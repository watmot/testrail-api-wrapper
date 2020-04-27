class EstimateMixin:
    @property
    def estimate(self):
        return self._data.get('estimate')

    @estimate.setter
    def estimate(self, arg):
        # TODO Add logic to handle timespan type
        self._data['estimate'] = str(arg)
