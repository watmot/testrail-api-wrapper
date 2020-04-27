from testrail.request import TestrailRequest


class DeleteMixin:
    def _delete(self, **parameters):
        """
        Delete the resource from TestRail
        :return: Response if request is a success
        """
        response = TestrailRequest.post(uri=self.ENDPOINTS['delete'].format(**parameters))

        return response

