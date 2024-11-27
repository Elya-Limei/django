from django.urls import path, re_path
from . import views
from .views import logout_view, logout_get_view

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    path('', views.index, name='index'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    path('logout/', logout_view, name='logout'),
    path('logout/get/', logout_get_view, name='logout_get'),
]



