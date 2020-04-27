from testrail.request import TestrailRequest


class UpdateMixin:
    def _update(self, **parameters):
        """
        Update the resource in TestRail
        :return: Response + Resource if request is a success
        """
        uri = self.ENDPOINTS['update'].format(**parameters)
        payload = self._filter_post_data('update')

        response = TestrailRequest.post(uri=uri, payload=payload)

        self._data.update(response.json())

        return response
