from django.urls import path
from . import views

urlpatterns = [
    path('otherapiview/books/', views.BookView.as_view()),
]