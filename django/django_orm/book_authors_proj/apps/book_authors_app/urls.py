from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books$', views.books),
    url(r'^authors$', views.authors),
    url(r'^books/(?P<get_id>\d+)$', views.show_book),
    url(r'^authors/(?P<get_id>\d+)$',views.show_author),
    url(r'^books/add$', views.add_book),
    url(r'^authors/add$', views.add_author),
    url(r'^authors/add_book/(?P<author_id>\d+)$', views.author_add_book),
    url(r'^books/add_author/(?P<book_id>\d+)$', views.book_add_author),
]