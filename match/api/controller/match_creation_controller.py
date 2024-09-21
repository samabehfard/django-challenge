from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from match.logic.match_logic import MatchLogic


class MatchView(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.match_logic = MatchLogic()

    def post(self, request):
        serializer = MatchSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        home_matches = serializer.data.get("home_matches")
        away_matches = serializer.data.get("away_matches")
        date = serializer.data.get("date")
        time = serializer.data.get("time")
        default_price = serializer.data.get("default_price")
        self.match_logic.add_match(
            home_matches=home_matches,
            away_matches=away_matches,
            date=date,
            time=time,
            default_price=default_price
        )
        return Response({'message': 'Match defined successfully'}, status=status.HTTP_201_CREATED)

    def get(self, request):
        matches = self.match_logic.get_all_matches()
        return Response({'matches': matches}, status=status.HTTP_201_CREATED)
