from django.urls import path
from . import views

urlpatterns = [
    path('genericviewset/books/', views.BookView.as_view({'get':'list', 'post':'create'})),
    path('genericviewset/books/<int:pk>/', views.BookView.as_view({'get':'retrieve', 'put':'update'})),
    path('genericviewset/books/<int:pk>/othermethod/', views.BookView.as_view({'get':'othermethod'})),
]