from rest_framework.generics import ListAPIView, CreateAPIView

from .models import Station, ChargePoint
from .serializers import StationSerializer


class StationListView(ListAPIView):
    """
    API endpoint that allows Charging Station to be viewed or edited.
    """
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class StationCreateView(CreateAPIView):
    """
    API endpoint for creating charging station
    """
    serializer_class = StationSerializer