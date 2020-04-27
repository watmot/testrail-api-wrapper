from testrail.request import TestrailRequest


class GetMixin:
    def __init__(self, **parameters):
        super().__init__()
        if parameters:
            self.get(**parameters)

    def get(self, **parameters):
        project_id = test_id = None

        if 'project_id' in parameters:
            project_id = parameters.pop('project_id')
        elif 'test_id' in parameters:
            test_id = parameters.pop('test_id')

        response = TestrailRequest.get(uri=self.ENDPOINTS['get'].format(project_id=project_id,
                                                                        test_id=test_id),
                                       parameters=parameters)
        data = response.json()

        self._data = [self.MODEL(data=i) for i in data] if data else []
