from rest_framework import serializers


class SeatReservationSerializer(serializers.Serializer):
    seat_codes = serializers.ListField(
        child=serializers.CharField(),
    )
    match_id = serializers.IntegerField()

class TicketCodeSerializer(serializers.Serializer):
    ticket_codes = serializers.ListField(
        child=serializers.CharField(),
    )
