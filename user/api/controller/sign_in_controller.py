from django.http import HttpResponseBadRequest
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from common.common_errors import BadRequestException
from common.common_serializer import CommonSerializer
from user.api.serializer.sign_in_serializer import UserLoginSerializer, UserLoginResponseSerializer


class SignInView(APIView):
    @extend_schema(
        request=UserLoginSerializer,
        responses={
            status.HTTP_200_OK: UserLoginResponseSerializer,
            status.HTTP_400_BAD_REQUEST: CommonSerializer,
            status.HTTP_500_INTERNAL_SERVER_ERROR: CommonSerializer
        },
        description="end point for login."
    )
    def post(self, request):
        try:
            serializer = UserLoginSerializer(request.data)
            if not serializer.is_valid():
                raise BadRequestException("bad request")

            username = serializer.data.get('username')
            password = serializer.data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except BadRequestException:
            return Response("bad request", status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            # error.args[0] should be log
            return Response({'detail': 'Internal Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
