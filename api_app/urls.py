from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^station/list/$', views.StationListView.as_view(), name="station_list"),
]