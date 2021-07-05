import json

from django.http import JsonResponse
from django.views import View

from .serializer import BookSerializer
from .models import BookInfo

class BookView(View):
    def get(self, request):
        books = BookInfo.objects.all()
        ser = BookSerializer(books, many=True)
        return JsonResponse(ser.data, safe=False)

    def post(self, request):
        # 1 获取数据
        json_dict = json.loads(request.body.decode())
        # 2 验证数据
        ser = BookSerializer(data=json_dict)
        ser.is_valid()
        # 4 返回结果
        return JsonResponse(ser.errors)