from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.common_serializer import CommonSerializer
from match.api.serializer.match_serializer import MatchCreationSerializer, MatchGetListSerializer
from match.logic.match_logic import MatchLogic


class MatchView(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.match_logic = MatchLogic()

    @extend_schema(
        request=MatchCreationSerializer,
        responses={
            status.HTTP_200_OK: CommonSerializer,
            status.HTTP_400_BAD_REQUEST: CommonSerializer,
            status.HTTP_500_INTERNAL_SERVER_ERROR: CommonSerializer
        },
        description="Endpoint to create a match with home and away teams, date, time, and default price."
    )
    def post(self, request):
        try:
            serializer = MatchCreationSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({"detail": "bad request"}, status=status.HTTP_400_BAD_REQUEST)
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
            return Response({'detail': 'Match defined successfully'}, status=status.HTTP_200_OK)
        except Exception as error:
            # error.args[0] should be log
            return Response({'detail': 'Internal Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        responses={
            status.HTTP_200_OK: MatchGetListSerializer,
            status.HTTP_500_INTERNAL_SERVER_ERROR: CommonSerializer
        },
        description="Endpoint to get all matches with their detail."
    )
    def get(self, request):
        try:
            matches = self.match_logic.get_all_matches()
            serializer = MatchGetListSerializer(data={'matches': matches})
            if not serializer.is_valid():
                # it should be logged and notify developers
                return Response({"detail": "Internal Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            # error.args[0] should be log
            return Response({'detail': 'Internal Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
