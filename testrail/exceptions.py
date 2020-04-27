class TestRailBaseException(Exception):
    pass  # TODO Docstrings


class TooManyRequestsError(TestRailBaseException):
    def __init__(self, delay, message):
        super().__init__(message)
        self.delay = delay
        #  TODO Docstrings


class MethodNotImplementedError(TestRailBaseException):
    pass  # TODO Docstrings


class UnableToResolveError(TestRailBaseException):
    pass  # TODO Docstrings
