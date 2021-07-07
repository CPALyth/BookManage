from django.urls import path
from . import views

urlpatterns = [
    path('modelviewset/books/', views.BookView.as_view({'get': 'list', 'post': 'create'})),
    path('modelviewset/books/<int:pk>/', views.BookView.as_view({'get': 'retrieve',
                                                                'put': 'update',
                                                                'delete': 'destroy'})),
]