from testrail.request import TestrailRequest


class BaseMethodMixin:
    pass


class AddMixin(BaseMethodMixin):
    def _add(self, endpoint_key='add', **parameters):
        response = TestrailRequest.post(uri=self.ENDPOINTS[endpoint_key].format(**parameters),
                                        payload=self._filter_post_data(endpoint_key))
        response_json = response.json()
        self._update_data(response_json)
        return response


class CloseMixin(BaseMethodMixin):
    def _close(self, endpoint_key='close', **parameters):
        """
        Close the resource in TestRail
        :return: Response if request is a success
        """
        response = TestrailRequest.post(uri=self.ENDPOINTS[endpoint_key].format(**parameters))
        response_json = response.json()
        self._update_data(response_json)
        return response


class DeleteMixin(BaseMethodMixin):
    def _delete(self, endpoint_key='delete', **parameters):
        """
        Delete the resource from TestRail
        :return: Response if request is a success
        """
        response = TestrailRequest.post(uri=self.ENDPOINTS[endpoint_key].format(**parameters))

        return response


class GetMixin(BaseMethodMixin):
    def __init__(self, new=False, data=None, **parameters):
        super().__init__(data=data)
        if not new and not data:
            self.get(**parameters)

    def _get(self, endpoint_key='get', **parameters):
        response = TestrailRequest.get(uri=self.ENDPOINTS[endpoint_key].format(**parameters))
        response_json = response.json()
        self._update_data(response_json)
        return response


class UpdateMixin(BaseMethodMixin):
    def _update(self, endpoint_key='update', **parameters):
        """
        Update the resource in TestRail
        :return: Response + Resource if request is a success
        """
        response = TestrailRequest.post(uri=self.ENDPOINTS[endpoint_key].format(**parameters),
                                        payload=self._filter_post_data(endpoint_key))
        response_json = response.json()
        self._update_data(response_json)
        return response



