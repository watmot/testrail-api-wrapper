from testrail.request import TestrailRequest


class GetMixin:
    @staticmethod
    def _parse_query_string(**kwargs):
        query_string = ''
        for k, v in kwargs.items():
            if v:
                query_string += f'&{k}={v}'
        return query_string

    def _get(self, endpoint_key='get', **parameters):
        response = TestrailRequest.get(uri=self.ENDPOINTS[endpoint_key].format(**parameters))
        response_json = response.json()
        self._data = [self.MODEL(data=i) for i in response_json] if response_json else []
        return response

    def _add(self, endpoint_key='add', **parameters):

        payload = [model._filter_post_data for model in self._data]

        response = TestrailRequest.post(uri=self.ENDPOINTS[endpoint_key].format(**parameters),
                                        payload=payload)

        response_json = response.json()

        self._data = [self.MODEL(data=i) for i in response_json]

        return response

