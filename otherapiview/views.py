from rest_framework.generics import ListAPIView

from view.models import BookInfo
from view.serializer import BookSerializer

class BookView(ListAPIView):

    queryset = BookInfo.objects.filter(is_delete=False)
    serializer_class = BookSerializer
