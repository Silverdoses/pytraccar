class TraccarApiException(Exception):

    def __init__(self, info):
        """
        Args:
            info: Message to append to the error
        """
        self.info = info

    def __str__(self):
        return 'Traccar API Error: {}'.format(self.info)


class ObjectAlreadyExistsException(TraccarApiException):
    def __init__(self, obj, obj_type):
        """
        Args:
            obj:
            obj_type:
        """
        message = '[{} {} already exists]'.format(obj, obj_type)
        super().__init__(info=message)


class ObjectNotFoundException(TraccarApiException):

    def __init__(self, obj, obj_type):
        """

        Args:
            obj:
            obj_type:
        """
        message = '[{}(s) {} not found]'.format(obj, obj_type)
        super().__init__(info=message)


class ForbiddenAccessException(TraccarApiException):

    def __init__(self):
        message = '[Access is denied]: Wrong username or password'
        super().__init__(info=message)


class UserPermissionException(TraccarApiException):

    def __init__(self):
        message = '[User has not enough permissions]'
        super().__init__(info=message)


class InvalidTokenException(TraccarApiException):

    def __init__(self):
        message = '[Invalid user token]'
        super().__init__(info=message)
