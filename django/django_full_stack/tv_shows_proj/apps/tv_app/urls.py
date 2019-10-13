from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add$', views.view_add_page),
    url(r'^add_show$', views.add_show),
    url(r'^view$', views.view_all),
    url(r'^(?P<get_id>\d+)/edit$', views.page_edit_show),
    url(r'^(?P<get_id>\d+)/$', views.view_show),
    url(r'^(?P<get_id>\d+)/show_edit$', views.edit_show),
    url(r'^(?P<get_id>\d+)/delete$', views.delete_show),

]