from django.urls import path, re_path
from . import views

urlpatterns = [
    path('books_drf', views.BookView.as_view())
]
