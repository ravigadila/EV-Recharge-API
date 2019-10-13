from django.db import models
from django.utils.translation import ugettext_lazy as _


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
    contact_name = models.CharField(max_length=200, blak=True, default="")
    phone_number = models.CharField(max_length=20, blak=True, default="")
    email = models.EmailField(_('email address'), blak=True, default="")
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=55)
    state = models.CharField(max_length=55, blak=True, default="")
    zip_code = models.CharField(max_length=20, blak=True, default="")
    country = models.CharField(max_length=55)
    landmark = models.CharField(max_length=55, blak=True, default="")
    geo_coords = models.PointField(null=True, blank=True)
    notes = models.CharField(max_length=1000, blak=True, default="")
    amenities = models.CharField(max_length=255, blak=True, default="")
    station_type = models.CharField(choices=STATION_TYPE, default="UNKNOWN")

    def __str__(self):
        return self.name

class ConnectorType(models.Model):
    name = models.CharField(max_length=200, unique=True, default="Wall Outlet")
    connector_image = models.ImageField(upload_to='connectors', blak=True, null=True)
    
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
    station = models.ForeignKey(Station, on_delete=models.SET_NULL)
    code = models.CharField(_('unique code of each point'), max_length=200)
    open_time = models.TimeField() # for 24X7 use 12 AM-12 AM
    close_time = models.TimeField()
    status = models.CharField(choices=POINT_STATUS, default="WORKING")
    cost_per_hr = models.DecimalField(max_digits=5, decimal_places=5, default=0)
    connector_type = models.ForeignKey(ConnectorType, on_delete=models.SET_NULL)
    compatibility = models.CharField(_('vehicle name'), max_length=255, blak=True, default="ALL") # vehicle name
    notes = models.CharField(max_length=255)
    power_output = models.FloatField(_('in kW'))

    def __str__(self):
        return self.code
