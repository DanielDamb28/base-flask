import pytest
from src.app import bcrypt, create_app
from src.models import db, User, Role

@pytest.fixture()
def app():
    app = create_app(enviroment='testing'
    )
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def access_token(client):
    role = Role(name="admin")
    db.session.add(role)
    db.session.commit()
    user = User(username="damb", password="test", role_id=role.id)
    password = user.password
    user.password = bcrypt.generate_password_hash(password).decode("utf-8")
    db.session.add(user)
    db.session.commit()

    result = client.post(
        "/auth/login/",
        json={"username": user.username, "password": password},
    )
    return result.json["access_token"]