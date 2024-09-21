from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ticket.logic.ticket_logic import TicketLogic


class TicketListView(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ticket_logic = TicketLogic()

    def post(self, request):
        serializer = TicketSerializer(data=request.data)
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
        return Response({'ticket_codes': ticket_codes}, status=status.HTTP_201_CREATED)
