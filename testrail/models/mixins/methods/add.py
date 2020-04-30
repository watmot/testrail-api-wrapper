from testrail.request import TestrailRequest


class AddMixin:
    def _add(self, **parameters):
        response = TestrailRequest.post(uri=self.ENDPOINTS['add'].format(**parameters),
                                        payload=self._filter_post_data('add'))
        response_json = response.json()
        self._update_data(response_json)
        return response
