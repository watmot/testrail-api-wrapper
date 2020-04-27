from testrail.request import TestrailRequest


class CloseMixin:
    def _close(self, **parameters):
        """
        Close the resource in TestRail
        :return: Response if request is a success
        """
        response = TestrailRequest.post(uri=self.ENDPOINTS['close'].format(**parameters))

        return response
