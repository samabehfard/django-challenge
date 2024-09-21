from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class UserLoginResponseSerializer(serializers.Serializer):
    token = serializers.CharField()
