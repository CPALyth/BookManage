from django.urls import path
from . import views

urlpatterns = [
    path('viewset/books/', views.BookView.as_view({'get':'list', 'post':'create'})),
    path('viewset/books/<int:pk>/', views.BookView.as_view({'get':'retrieve', 'put':'update'})),
    path('viewset/books/<int:pk>/othermethod/', views.BookView.as_view({'get':'othermethod'})),
]