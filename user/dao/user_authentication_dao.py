from user.models import User


class UserAuthenticationDao:
    def is_username_duplicate(self, username):
        user = User.objects.filter(username=username).first()
        if user:
            return True
        else:
            return False

    def is_identity_number_duplicate(self, identity_number):
        user = User.objects.filter(identity_number=identity_number).first()
        if user:
            return True
        else:
            return False

    def sign_up(
            self,
            username,
            name,
            family_name,
            identity_number,
            phone_number,
            password
    ):
        user = User.objects.create(
            username=username,
            name=name,
            family_name=family_name,
            identity_number=identity_number,
            phone_number=phone_number,
            password=password)

        user.set_password(password)
        user.save()