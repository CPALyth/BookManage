from django.urls import path
from . import views

urlpatterns = [
    path('viewset/book/', views.BookView.as_view({'get':'list', 'post':'create'})),
    path('viewset/book/<int:pk>/', views.BookView.as_view({'get':'retrieve', 'put':'update'})),
    path('viewset/book/<int:pk>/othermethod/', views.BookView.as_view({'get':'othermethod'})),
]