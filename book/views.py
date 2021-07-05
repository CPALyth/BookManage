import json

from django.http import JsonResponse
from django.views import View

from .serializer import BookSerializer
from .models import BookInfo

class BooksView(View):
    def get(self, request):
        """获取所有图书"""
        books = BookInfo.objects.all()
        ser = BookSerializer(books, many=True)
        return JsonResponse(ser.data, safe=False)

    def post(self, request):
        """添加单个图书"""
        # 1 获取数据
        json_dict = json.loads(request.body.decode())
        # 2 验证数据
        ser = BookSerializer(data=json_dict)
        # 3 保存数据
        if ser.is_valid():
            ser.save()
        # 4 返回结果
        return JsonResponse(ser.errors)