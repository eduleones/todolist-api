from .base import BaseException


class TaskNotFoundException(BaseException):
    def __init__(self, error_code=None, message=None):
        super().__init__(error_code, message)


class InvalidTaskException(BaseException):
    def __init__(self, error_code=None, message=None):
        super().__init__(error_code, message)
