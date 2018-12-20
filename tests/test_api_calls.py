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


@pytest.fixture(scope='module')
def admin_session():
    admin = api.TraccarAPI(base_url=test_url)
    admin.login_with_token(token=admin_token)
    return admin


@pytest.fixture(scope='module')
def user_session():
    user = api.TraccarAPI(base_url=test_url)
    user.login_with_token(token=user_token)
    return user


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


def test_api_users_with_user(user_session):
    user = user_session

    # Test not enough permissions
    with pytest.raises(UserPermissionException):
        user.get_all_devices()

    # Test non-existent device
    with pytest.raises(ObjectNotFoundException):
        user.get_devices(query='uniqueId', params=['NotADevice'])

    task1 = user.create_device(name='Test Device', unique_id='testdevice')
    task2 = user.get_devices()
    task3 = user.get_devices(query='id', params=[1])
    task4 = user.get_devices(query='uniqueId', params=['testdevice'])

    assert type(task1) == dict
    assert type(task2) == list
    assert type(task3) == list
    assert type(task4) == list

    # Test duplicated device
    with pytest.raises(ObjectAlreadyExistsException):
        user.create_device(name='Test Device', unique_id='testdevice')


def test_api_users_with_admin(admin_session):
    admin = admin_session
    task1 = admin.get_all_devices()
    assert type(task1) == list
