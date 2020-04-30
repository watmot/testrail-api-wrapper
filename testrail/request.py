import logging
import os
import requests

from testrail.decorators import retry
from testrail.exceptions import TooManyRequestsError


class TestrailRequest:
    AUTH = (os.environ["TESTRAIL_USER"], os.environ["TESTRAIL_KEY"])
    URL = os.environ["TESTRAIL_URL"]
    HEADERS = {"Content-Type": "application/json"}

    @classmethod
    @retry
    def _request(cls, method, uri=None, payload=None):
        response = method(url=cls.URL + uri,
                          auth=cls.AUTH,
                          headers=cls.HEADERS,
                          data=payload)

        if response.status_code == 429:
            raise TooManyRequestsError(delay=response.headers['Retry-After'])
        elif response.status_code >= 300:
            response.raise_for_status()

        return response

    @classmethod
    def get(cls, uri=None):
        response = cls._request(method=requests.get,
                                uri=uri)
        return response

    @classmethod
    def post(cls, uri=None, payload=None):
        response = cls._request(method=requests.post,
                                uri=uri,
                                payload=payload)
        return response
