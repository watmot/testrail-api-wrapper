from testrail.request import TestrailRequest


class GetMixin:
    def __init__(self, **parameters):
        super().__init__()
        self.get(**parameters)

    @staticmethod
    def _parse_query_string(**kwargs):
        query_string = ''
        for k, v in kwargs.items():
            if v:
                query_string += f'&{k}={v}'
        return query_string

    def _get(self, **parameters):
        response = TestrailRequest.get(uri=self.ENDPOINTS['get'].format(**parameters))
        response_json = response.json()
        self._data = [self.MODEL(data=i) for i in response_json] if response_json else []
        return response
