from rest_framework import serializers


class StadiumCreationSerializer(serializers.Serializer):
    potential = serializers.IntegerField()
    address = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=100)

class StadiumGetSerializer(serializers.Serializer):
    potential = serializers.IntegerField()
    address = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=100)

class StadiumGetListSerializer(serializers.Serializer):
    stadiums = StadiumGetSerializer(many=True)