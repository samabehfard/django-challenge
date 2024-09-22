from django.http import HttpResponseBadRequest
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from common.common_errors import BadRequestException
from common.common_serializer import CommonSerializer
from user.api.serializer.signup_serializer import UserSignUpSerializer
from user.errors import DuplicateUserNameException, DuplicateIdentityNumberException
from user.logic.user_authentication_logic import UserAuthenticationLogic


class SignUpView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_authentication_logic = UserAuthenticationLogic()
    @extend_schema(
        request=UserSignUpSerializer,
        responses={
            status.HTTP_200_OK: CommonSerializer,
            status.HTTP_400_BAD_REQUEST: CommonSerializer,
            status.HTTP_500_INTERNAL_SERVER_ERROR: CommonSerializer
        },
        description="end point for login."
    )
    def post(self, request):
        try:
            serializer = UserSignUpSerializer(data=request.data)
            if not serializer.is_valid():
                raise BadRequestException("bad request")
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
            return Response({'detail': 'User created successfully'}, status=status.HTTP_200_OK)
        except BadRequestException:
            return Response("bad request", status=status.HTTP_400_BAD_REQUEST)
        except DuplicateIdentityNumberException:
            # we should log this but we should not show our existed identity numbers to other users
            return Response("bad request", status=status.HTTP_400_BAD_REQUEST)

        except DuplicateUserNameException:
            return Response("duplicate username", status=status.HTTP_409_CONFLICT)

        except Exception as error:
            return Response("internal error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

