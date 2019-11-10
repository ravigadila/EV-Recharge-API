from django.contrib import admin
from .models import Station, ChargePoint, ConnectorType

admin.site.register(Station)
admin.site.register(ChargePoint)
admin.site.register(ConnectorType)
