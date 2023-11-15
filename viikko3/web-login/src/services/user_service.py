import re

from entities.user import User
from repositories.user_repository import user_repository as default_user_repository


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class InvalidUsernameError(Exception):
    pass


class InvalidPasswordError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(User(username, password))

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if self._user_repository.find_by_username(username):
            raise InvalidUsernameError("Username is already taken")

        if len(username) < 3:
            raise InvalidUsernameError("Minimum length of username is 3")

        if not re.match("^[a-z]+$", username):
            raise InvalidUsernameError("Username should only contain lowercase letters")

        if len(password) < 8:
            raise InvalidPasswordError("Minimum length of password is 8")

        if re.match("^([a-z]|[A-Z])*$", password):
            raise InvalidPasswordError("Password should not contain only letters")

        if password != password_confirmation:
            raise InvalidPasswordError("Password and confirmation don't match")

user_service = UserService()
