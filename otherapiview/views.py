from rest_framework.generics import ListAPIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from view.models import BookInfo
from view.serializer import BookSerializer

class BookView(ListAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    queryset = BookInfo.objects.filter(is_delete=False)
    serializer_class = BookSerializer
