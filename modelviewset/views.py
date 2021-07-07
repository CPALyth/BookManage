from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from view.models import BookInfo
from view.serializer import BookSerializer

class BookView(ModelViewSet):
    queryset = BookInfo.objects.filter(is_delete=False)
    serializer_class = BookSerializer