from django.urls import path
from . import views

urlpatterns = [
    path('genericapiview/books/', views.BooksView.as_view()),
    path('genericapiview/book/<int:pk>/', views.BookView.as_view()),
]