from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^log_reg$', views.log_reg),
    url(r'^main$', views.main),
    url(r'^logout$', views.logout),
    url(r'^add_book$',views.add),
    url(r'^view_edit/(?P<book_id>\d+)$', views.view_edit),
    url(r'^update/(?P<book_id>\d+)$', views.update),
    url(r'^delete/(?P<book_id>\d+)$', views.delete),
    url(r'^fave_book/(?P<book_id>\d+)$', views.add_fave),



]