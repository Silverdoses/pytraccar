from pytraccar.exceptions import (
    ForbiddenAccessException,
    InvalidTokenException,
    ObjectAlreadyExistsException,
    ObjectNotFoundException,
    UserPermissionException
)
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


def test_create_device():
    user = api.TraccarAPI(base_url=test_url)
    user.login_with_token(token=admin_token)
    result = user.create_device(name='Test Device', unique_id='testdevice')
    assert type(result) == dict


def test_create_duplicated_device():
    with pytest.raises(ObjectAlreadyExistsException):
        user = api.TraccarAPI(base_url=test_url)
        user.login_with_token(token=admin_token)
        user.create_device(name='Test Device', unique_id='testdevice')


def test_get_devices():
    user = api.TraccarAPI(base_url=test_url)
    user.login_with_token(token=admin_token)
    result_by_user_id = user.get_devices()
    result_by_id = user.get_devices(query='id', params=[1])
    result_by_unique_id = user.get_devices(query='uniqueId', params=['testdevice'])

    assert type(result_by_user_id) == list
    assert type(result_by_id) == list
    assert type(result_by_unique_id) == list


def test_device_does_not_exist():
    with pytest.raises(ObjectNotFoundException):
        user = api.TraccarAPI(base_url=test_url)
        user.login_with_token(token=admin_token)
        user.get_devices(query='uniqueId', params=['NotADevice'])


def test_update_device():
    user = api.TraccarAPI(base_url=test_url)
    user.login_with_token(token=admin_token)
    result = user.update_device(device_id=1, name='ANewName')
    assert type(result) == list
