from rest_framework import serializers
from .models import Station, ChargePoint, ConnectorType


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = [
            'station_name', 'contact_name', 'phone_number',
            'email', 'address', 'city',
            'state', 'zip_code', 'country',
            'landmark', 'latitude', 'longitude',
            'notes', 'amenities', 'station_type',
            'created_by', 'created_at', 'updated_at'
        ]
        extra_kwargs = {
            'created_by': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True}
        }