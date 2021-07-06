from django.urls import path
from . import views

urlpatterns = [
    path('apiview/books/', views.BooksView.as_view()),
    path('apiview/book/<int:pk>/', views.BookView.as_view()),
]
