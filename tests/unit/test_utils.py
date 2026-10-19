from src.utils import eleva_quadrado, required_role
from unittest.mock import Mock, patch
import pytest
from http import HTTPStatus

def test_required_role_sucess(mocker):
    mock_user = mocker.Mock()
    mock_user.role.name = "admin"

    mocker.patch('src.utils.get_jwt_identity')
    mocker.patch('src.utils.db.get_or_404', return_value=mock_user)
    decorated_function = required_role("admin")(lambda: "success")
    result = decorated_function()

    assert result == "success"


def test_required_role_fail(mocker):
    mock_user = mocker.Mock()
    mock_user.role.name = "normal"
    
    mocker.patch('src.utils.get_jwt_identity')
    mocker.patch('src.utils.db.get_or_404', return_value=mock_user)
    decorated_function = required_role("admin")(lambda: "success")

    result = decorated_function()

    assert result == ({"message": "User don't have acess."}, HTTPStatus.FORBIDDEN)
