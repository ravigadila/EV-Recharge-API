from django.conf.urls import url
from api_app.views import station

urlpatterns = [
    url(r'^station/list/$', station.StationListView.as_view(), name="station_list"),
    url(r'^station/create/$', station.StationCreateView.as_view(), name="station_create"),
    url(r'^station/(?P<pk>\d+)/$', station.StationUpdateView.as_view(), name="station_create"),
]
