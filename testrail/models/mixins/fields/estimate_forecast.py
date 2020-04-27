class EstimateForecastMixin:
    @property
    def estimate_forecast(self):
        return self._data.get('estimate_forecast')
