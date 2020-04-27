from testrail.request import TestrailRequest


class GetMixin:
    def __init__(self, **parameters):
        super().__init__()
        if parameters:
            self.get(**parameters)

    def _get(self, **parameters):
        response = TestrailRequest.get(uri=self.ENDPOINTS['get'].format(**parameters))

        return response
