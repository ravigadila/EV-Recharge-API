from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from api_app.models import Station, ChargePoint
from api_app.serializers import StationSerializer


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


class StationUpdateView(RetrieveUpdateDestroyAPIView):
    """
    API for Update, Delete, Get Station.
    """
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    lookup_field = 'pk'
