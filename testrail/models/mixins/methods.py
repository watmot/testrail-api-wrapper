from testrail.request import TestrailRequest


class BaseMethodMixin:
    @staticmethod
    def _generate_key(field=None, master=None):
        key = f'{master}_{field}' if field else master
        return key


class AddMixin(BaseMethodMixin):
    def _add(self, field=None, **parameters):
        master_key = 'add'
        key = self._generate_key(field=field, master=master_key)
        response = TestrailRequest.post(uri=self.ENDPOINTS[key].format(**parameters),
                                        payload=self._filter_post_data(master_key))
        response_json = response.json()
        self._update_data(response_json)
        return response


class CloseMixin(BaseMethodMixin):
    def _close(self, field=None, **parameters):
        """
        Close the resource in TestRail
        :return: Response if request is a success
        """
        master_key = 'close'
        key = self._generate_key(field=field, master=master_key)
        response = TestrailRequest.post(uri=self.ENDPOINTS[key].format(**parameters))
        response_json = response.json()
        self._update_data(response_json)
        return response


class DeleteMixin(BaseMethodMixin):
    def _delete(self, field=None, **parameters):
        """
        Delete the resource from TestRail
        :return: Response if request is a success
        """
        master_key = 'delete'
        key = self._generate_key(field=field, master=master_key)
        response = TestrailRequest.post(uri=self.ENDPOINTS[key].format(**parameters))

        return response


class GetMixin(BaseMethodMixin):
    def __init__(self, data=None, **parameters):
        super().__init__(data=data)
        if parameters:
            self._get(**parameters)

    def _get(self, field=None, **parameters):
        master_key = 'get'
        key = self._generate_key(field=field, master=master_key)
        response = TestrailRequest.get(uri=self.ENDPOINTS[key].format(**parameters))
        response_json = response.json()
        self._update_data(response_json)
        return response


class UpdateMixin(BaseMethodMixin):
    def _update(self, field=None, **parameters):
        """
        Update the resource in TestRail
        :return: Response + Resource if request is a success
        """
        master_key = 'update'
        key = self._generate_key(field=field, master=master_key)
        response = TestrailRequest.post(uri=self.ENDPOINTS[key].format(**parameters),
                                        payload=self._filter_post_data(master_key))
        response_json = response.json()
        self._update_data(response_json)
        return response



