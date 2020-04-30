from testrail.request import TestrailRequest


class UpdateMixin:
    def _update(self, **parameters):
        """
        Update the resource in TestRail
        :return: Response + Resource if request is a success
        """

        response = TestrailRequest.post(uri=self.ENDPOINTS['update'].format(**parameters),
                                        payload=self._filter_post_data('update'))
        response_json = response.json()
        self._update_data(response_json)
        return response
