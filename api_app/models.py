from django.db import models
from django.utils.translation import ugettext_lazy as _
from dashboard.models import User

STATION_TYPE = (
    ("HOME", _("Home")),
    ("COMMERCIAL", _("Commercial")),
    ("UNKNOWN", _("unknown")),
    ("SHOPPING_MALL", _("SHOPPING_MALL")),
)

class Station(models.Model):
    """Charge station or location
    """
    station_name = models.CharField(max_length=200, unique=True)
    contact_name = models.CharField(max_length=200, blank=True, default="")
    phone_number = models.CharField(max_length=20, blank=True, default="")
    email = models.EmailField(_('email address'), blank=True, default="")
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=55)
    state = models.CharField(max_length=55, blank=True, default="")
    zip_code = models.CharField(max_length=20, blank=True, default="")
    country = models.CharField(max_length=55)
    landmark = models.CharField(max_length=55, blank=True, default="")
    latitude = models.DecimalField(max_digits=10, decimal_places=10, default=0)
    longitude = models.DecimalField(max_digits=10, decimal_places=10, default=0)
    notes = models.CharField(max_length=1000, blank=True, default="")
    amenities = models.CharField(max_length=255, blank=True, default="")
    station_type = models.CharField(choices=STATION_TYPE, default="UNKNOWN", max_length=55)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ConnectorType(models.Model):
    name = models.CharField(max_length=200, unique=True, default="Wall Outlet")
    connector_image = models.ImageField(upload_to='connectors', blank=True, null=True)
    
    def __str__(self):
        return self.name

POINT_STATUS = (
    ("WORKING", _("WORKING")),
    ("COMING_SOON", _("COMING_SOON")),
    ("IN_REPAIR", _("In Repair/Not Funtioning")),
    ("REMOVED", _("REMOVED"))
)

class ChargePoint(models.Model):
    """Each charge station can have multiple chargepoints
    """
    station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True)
    code = models.CharField(_('unique code of each point'), max_length=200)
    open_time = models.TimeField() # for 24X7 use 12 AM-12 AM
    close_time = models.TimeField()
    status = models.CharField(choices=POINT_STATUS, default="WORKING", max_length=55)
    cost_per_hr = models.DecimalField(max_digits=5, decimal_places=5, default=0)
    connector_type = models.ForeignKey(ConnectorType, on_delete=models.SET_NULL, null=True)
    compatibility = models.CharField(_('vehicle name'), max_length=255, blank=True, default="ALL") # vehicle name
    notes = models.CharField(max_length=255)
    power_output = models.FloatField(_('in kW'))
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code
