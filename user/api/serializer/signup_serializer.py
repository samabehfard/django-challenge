from rest_framework import serializers


class UserSignUpSerializer(serializers.Serializer):
    def create(self, validated_data):
        ...

    def update(self, instance, validated_data):
        ...

    username = serializers.CharField()
    name = serializers.CharField()
    family_name = serializers.CharField()
    identity_number = serializers.CharField()
    phone_number = serializers.CharField()
    password = serializers.CharField()

