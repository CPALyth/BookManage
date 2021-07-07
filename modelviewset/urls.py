from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter

from . import views

urlpatterns = []

router = DefaultRouter()
router.register('modelviewset', views.BookView, basename='books')
print(router.urls)
urlpatterns += router.urls
