from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Stadium.api.serializer.stadium_serializer import StadiumCreationSerializer, StadiumGetListSerializer
from Stadium.logic.stadium_logic import StadiumLogic
from common.common_serializer import CommonSerializer


class StadiumListView(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stadium_logic = StadiumLogic()

    @extend_schema(
        request=StadiumCreationSerializer,
        responses={
            status.HTTP_200_OK: CommonSerializer,
            status.HTTP_400_BAD_REQUEST: CommonSerializer,
            status.HTTP_500_INTERNAL_SERVER_ERROR: CommonSerializer
        },
        description="Endpoint to create a Stadium."
    )
    def post(self, request):
        try:
            serializer = StadiumCreationSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            potential = serializer.data.get("potential")
            address = serializer.data.get("address")
            name = serializer.data.get("name")
            self.stadium_logic.add_stadium(
                potential=potential,
                address=address,
                name=name,
            )
            return Response({'detail': 'Stadium defined successfully'}, status=status.HTTP_200_OK)
        except Exception as error:
            # error.args[0] should be log
            return Response({'detail': 'Internal Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @extend_schema(
        responses={
            status.HTTP_200_OK: StadiumGetListSerializer,
            status.HTTP_500_INTERNAL_SERVER_ERROR: CommonSerializer
        },
        description="Endpoint to show all submited stadiums."
    )
    def get(self, request):
        try:
            stadiums = self.stadium_logic.get_all_stadiums()
            serializer = StadiumGetListSerializer(data={'stadiums': stadiums})
            if not serializer.is_valid():
                # it should be logged and notify developers
                return Response({"detail": "Internal Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            # error.args[0] should be log
            return Response({'detail': 'Internal Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
