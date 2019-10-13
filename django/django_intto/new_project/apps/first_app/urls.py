from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<my_val>\d+)$',views.show),
    url(r'^(?P<val>\d+)/edit', views.edit),
    url(r'^(?P<val>\d+)/delete', views.destroy)
]