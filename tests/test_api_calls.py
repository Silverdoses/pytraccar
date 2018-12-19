from pytraccar.exceptions import InvalidTokenException
from pytraccar.exceptions import ForbiddenAccessException
from pytraccar.exceptions import UserPermissionException
import pytraccar.api as api
import pytest

username, correct_password = 'admin', 'admin'
wrong_password = 'WrongPassword'
user_token = '12345678901234567890ABCDEFGHIJKL'
admin_token = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ012345'
invalid_token = 'ThisIsNotAValidToken'
test_url = 'http://127.0.0.1:8082'


def test_valid_login_with_credentials():
    user = api.TraccarAPI(base_url=test_url)
    result = user.login_with_credentials(username, correct_password)
    assert type(result) == dict


def test_failed_login_with_credentials():
    with pytest.raises(ForbiddenAccessException):
        user = api.TraccarAPI(base_url=test_url)
        user.login_with_credentials(username, wrong_password)


def test_valid_login_with_token():
    user = api.TraccarAPI(base_url=test_url)
    user.login_with_token(token=admin_token)


def test_invalid_token_exception():
    with pytest.raises(InvalidTokenException):
        user = api.TraccarAPI(base_url=test_url)
        user.login_with_token(token=invalid_token)


def test_admin_get_all_devices():
    admin = api.TraccarAPI(base_url=test_url)
    admin.login_with_token(token=admin_token)
    result = admin.get_all_devices()
    assert type(result) == list


def test_user_get_all_devices():
    with pytest.raises(UserPermissionException):
        user = api.TraccarAPI(base_url=test_url)
        user.login_with_token(token=user_token)
        user.get_all_devices()
