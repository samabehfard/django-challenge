from rest_framework import serializers

class CommonSerializer(serializers.Serializer):
    def create(self, validated_data):
        ...

    def update(self, instance, validated_data):
        ...

    detail = serializers.CharField(max_length=255)
