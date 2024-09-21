from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Stadium.logic.stadium_logic import StadiumLogic


class StadiumListView(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stadium_logic = StadiumLogic()

    def post(self, request):
        serializer = StadiumSerializer(data=request.data)
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
        return Response({'message': 'Match defined successfully'}, status=status.HTTP_201_CREATED)

    def get(self, request):
        stadiums = self.stadium_logic.get_all_stadiums()
        return Response({'stadiums': stadiums}, status=status.HTTP_200_OK)
