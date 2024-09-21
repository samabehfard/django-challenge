from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.common_serializer import CommonSerializer
from ticket.api.serializer.ticket_serializer import SeatReservationSerializer, TicketCodeSerializer
from ticket.logic.ticket_logic import TicketLogic


class TicketListView(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ticket_logic = TicketLogic()

    @extend_schema(
        request=SeatReservationSerializer,
        responses={
            status.HTTP_200_OK: TicketCodeSerializer,
            status.HTTP_400_BAD_REQUEST: CommonSerializer,
            status.HTTP_500_INTERNAL_SERVER_ERROR: CommonSerializer
        },
        description="Endpoint to buy ticket / reserve seats /create ticket "
    )
    def post(self, request):
        try:
            serializer = SeatReservationSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            seat_codes = serializer.data.get("seat_codes")
            match_id = serializer.data.get("match_id")
            user = request.user
            ticket_codes = self.ticket_logic.buy_ticket(
                seat_codes=seat_codes,
                match_id=match_id,
                user=user,
            )
            serializer = TicketCodeSerializer(data={'ticket_codes': ticket_codes})
            if not serializer.is_valid():
                # it should be logged and notify developers
                return Response({"detail": "Internal Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            # error.args[0] should be log
            return Response({'detail': 'Internal Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
