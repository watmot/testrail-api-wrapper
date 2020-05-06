from testrail.request import TestrailRequest


class AddMixin:
    def _add(self, **parameters):
        response = TestrailRequest.post(uri=self.ENDPOINTS['add'].format(**parameters),
                                        payload=self._filter_post_data('add'))
        response_json = response.json()
        self._update_data(response_json)
        return response


class CloseMixin:
    def _close(self, **parameters):
        """
        Close the resource in TestRail
        :return: Response if request is a success
        """
        response = TestrailRequest.post(uri=self.ENDPOINTS['close'].format(**parameters))
        response_json = response.json()
        self._update_data(response_json)
        return response


class DeleteMixin:
    def _delete(self, **parameters):
        """
        Delete the resource from TestRail
        :return: Response if request is a success
        """
        response = TestrailRequest.post(uri=self.ENDPOINTS['delete'].format(**parameters))

        return response


class GetMixin:
    def __init__(self, data=None, **parameters):
        super().__init__(data=data)
        if parameters:
            self._get(**parameters)

    def _get(self, field=None, **parameters):
        key = f'get_{field}' if field else 'get'
        response = TestrailRequest.get(uri=self.ENDPOINTS[key].format(**parameters))
        response_json = response.json()
        self._update_data(response_json)
        return response


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



