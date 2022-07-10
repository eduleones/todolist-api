class BaseException(Exception):
    def __init__(self, error_code=None, message=None):
        self.error_code = error_code
        self.message = message
