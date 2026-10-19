from src.utils import required_role
from unittest.mock import Mock, patch
from http import HTTPStatus


def test_required_role_sucess():
    mock_user = Mock()
    mock_user.role.name = "admin"

    with patch('src.utils.get_jwt_identity'), patch(
        'src.utils.db.get_or_404', return_value=mock_user
    ):
        decorated_function = required_role("admin")(lambda: "success")
        result = decorated_function()

    assert result == "success"


def test_required_role_fail():
    mock_user = Mock()
    mock_user.role.name = "normal"

    with patch('src.utils.get_jwt_identity'), patch(
        'src.utils.db.get_or_404', return_value=mock_user
    ):
        decorated_function = required_role("admin")(lambda: "success")
        result = decorated_function()

    assert result == ({"message": "User don't have acess."}, HTTPStatus.FORBIDDEN)
