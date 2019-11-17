from rest_framework import serializers
from .models import Station, ChargePoint, ConnectorType


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = [
            'station_name', 'contact_name', 'phone_number',
            'email', 'address', 'city',
            'state', 'zip_code', 'country',
            'landmark', 'longitude', 'notes',
            'amenities', 'station_type',
        ]
        read_only_fields = ['created_by', 'created_at', 'updated_at']
