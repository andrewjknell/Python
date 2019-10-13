from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.show),
    url(r'^gold$', views.gold),
    url(r'^reset', views.reset),
]