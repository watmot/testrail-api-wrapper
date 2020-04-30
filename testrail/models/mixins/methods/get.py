from testrail.request import TestrailRequest


class GetMixin:
    def __init__(self, data=None, **parameters):
        super().__init__(data=data)
        if parameters:
            self._get(**parameters)

    def _get(self, **parameters):
        response = TestrailRequest.get(uri=self.ENDPOINTS['get'].format(**parameters))
        response_json = response.json()
        self._update_data(response_json)
        return response
