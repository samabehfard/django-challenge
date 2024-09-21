from django.http import HttpResponseBadRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.api.serializer.signup_serializer import UserSignUpSerializer
from user.errors import DuplicateIdentityNumber, DuplicateUserName
from user.logic.user_authentication_logic import UserAuthenticationLogic


class SignUpView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_authentication_logic = UserAuthenticationLogic()

    def post(self, request):
        try:
            serializer = UserSignUpSerializer(data=request.data)
            if not serializer.is_valid():
                raise HttpResponseBadRequest("bad request")
            username = serializer.data.get('username')
            name = serializer.data.get('name')
            family_name = serializer.data.get('family_name')
            identity_number = serializer.data.get('identity_number')
            phone_number = serializer.data.get('phone_number')
            password = serializer.data.get('password')
            self.user_authentication_logic.sign_up(
                username=username,
                name=name,
                family_name=family_name,
                identity_number=identity_number,
                phone_number=phone_number,
                password=password
            )
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        except HttpResponseBadRequest:
            return Response("bad request", status=status.HTTP_400_BAD_REQUEST)
        except DuplicateIdentityNumber:
            # we should log this but we should not show our existed identity numbers to other users
            return Response("bad request", status=status.HTTP_400_BAD_REQUEST)

        except DuplicateUserName:
            return Response("duplicate username", status=status.HTTP_409_CONFLICT)

        except:
            return Response("internal error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

