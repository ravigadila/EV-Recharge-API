from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

STATION_TYPE = (
    ("HOME", _("Home")),
    ("COMMERCIAL", _("Commercial")),
    ("SHOPPING_MALL", _("SHOPPING_MALL")),
    ("RESTAURANT", _("RESTAURANT")),
    ("OTHER", _("OTHER")),
)

CURRENT_STATUS = (
    ("ACTIVE", _("ACTIVE")),
    ("REMOVED", _("REMOVED")),
    ("MAINTENANCE", _("MAINTENANCE")),
)


class Station(models.Model):
    """Charge station or location
    """
    station_name = models.CharField(_('Name Of charging station'), max_length=200, unique=True)
    brand = models.CharField(_('charging station brand'), max_length=200, unique=True)
    phone_number = models.CharField(_('Phone Number of person'), max_length=20, blank=True, default="")
    email = models.EmailField(_('email address of station'), blank=True, default="")
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=55)
    state = models.CharField(max_length=55, blank=True, default="")
    zip_code = models.CharField(max_length=20, blank=True, default="")
    country = models.CharField(max_length=55)
    landmark = models.CharField(max_length=100, blank=True, default="")
    location_point = models.PointField(null=True, blank=True)
    notes = models.CharField(_('Extra details(optional)'), max_length=1000, blank=True, default="")
    amenities = models.CharField(max_length=255, blank=True, default="")
    station_type = models.CharField(choices=STATION_TYPE, default="UNKNOWN", max_length=55)
    status = models.CharField(choices=CURRENT_STATUS, default="ACTIVE", max_length=55)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

POINT_STATUS = (
    ("AVAILABLE", _("AVAILABLE")),
    ("IN_USE", _("IN_USE")),
    ("COMING_SOON", _("COMING_SOON")),
    ("IN_REPAIR", _("In Repair/Not Funtioning")),
    ("REMOVED", _("REMOVED"))
)

ACCESS_TYPE = (
    ("RESTRICTED", _("RESTRICTED")),
    ("PUBLIC", _("PUBLIC")),
)

PAYMENT_METHOD = (
    ("FREE", _("FREE")),
    ("REQUIRE_PAYMENT", _("REQUIRE_PAYMENT")),
    ("SUBSCRIPTION", _("SUBSCRIPTION")),
)

class Connector(models.Model):
    """Each charge station can have multiple chargepoints
    """
    station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True)
    connector_name = models.CharField(_('unique code of each point'), max_length=200)
    open_time = models.TimeField() # for 24X7 use 12 AM-12 AM
    close_time = models.TimeField()
    status = models.CharField(choices=POINT_STATUS, default="WORKING", max_length=55)
    cost_per_hr = models.DecimalField(max_digits=5, decimal_places=5, default=0)
    compatibility = models.CharField(_('vehicle name'), max_length=255, blank=True, default="ALL") # vehicle name
    fixed_cable = models.BooleanField(default=False)
    accessibility_type = models.CharField(choices=ACCESS_TYPE, default="PUBLIC", max_length=25)
    notes = models.CharField(max_length=255)
    chargeCapacity = models.FloatField(_('in kW'))
    payment_methods = models.CharField(choices=PAYMENT_METHOD, default="REQUIRE_PAYMENT", max_length=25)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.connector_name
