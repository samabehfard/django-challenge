from rest_framework import serializers


class MatchCreationSerializer(serializers.Serializer):
    def create(self, validated_data):
        ...

    def update(self, instance, validated_data):
        ...

    home_matches = serializers.CharField(max_length=255)
    away_matches = serializers.CharField(max_length=255)
    date = serializers.DateField()
    time = serializers.TimeField()
    default_price = serializers.IntegerField()
    stadium_id = serializers.IntegerField()


class MatchGetSerializer(serializers.Serializer):
    home_matches = serializers.CharField(max_length=255)
    away_matches = serializers.CharField(max_length=255)
    date = serializers.DateField()
    time = serializers.TimeField()
    default_price = serializers.IntegerField()


class MatchGetListSerializer(serializers.Serializer):
    matches = MatchGetSerializer(many=True)
