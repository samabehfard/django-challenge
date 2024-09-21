from user.dao.user_authentication_dao import UserAuthenticationDao
from user.errors import DuplicateUserName, DuplicateIdentityNumber


class UserAuthenticationLogic:
    def __init__(self):
        self.user_authentication_dao = UserAuthenticationDao()

    def sign_up(
            self,
            username,
            name,
            family_name,
            identity_number,
            phone_number,
            password
    ):
        if self.user_authentication_dao.is_username_duplicate(username):
            raise DuplicateUserName("username is duplicate")

        if self.user_authentication_dao.is_identity_number_duplicate(identity_number):
            raise DuplicateIdentityNumber("identity number is duplicate")

        self.user_authentication_dao.sign_up(
            username=username,
            name=name,
            family_name=family_name,
            identity_number=identity_number,
            phone_number=phone_number,
            password=password
        )
