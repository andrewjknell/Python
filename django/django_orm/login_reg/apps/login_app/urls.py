from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'login$', views.login),
    url(r'^success$', views.success),
    url(r'^registered$', views.registered),
    url(r'^wall$', views.view_wall),
    url(r'^logout$', views.logout),
    url(r'^post_message/(?P<user_id>\d+)$', views.post_message),
    url(r'^post_comment/(?P<message_id>\d+)$', views.post_comment),
]