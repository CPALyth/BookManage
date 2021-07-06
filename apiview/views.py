from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from view.models import BookInfo
from view.serializer import BookSerializer

class BooksView(APIView):
    """获取所有, 新增图书"""
    def get(self, request: Request):
        """获取所有图书"""
        print(request.query_params)
        books = BookInfo.objects.filter(is_delete=False)
        ser = BookSerializer(books, many=True)  # 返回多个对象, 要把many设为True
        return Response(ser.data)

    def post(self, request: Request):
        """新增单个图书"""
        # 1 获取数据
        json_dict = request.data
        # 2 验证数据
        ser = BookSerializer(data=json_dict)
        ser.is_valid()
        # 3 保存数据
        ser.save()
        # 4 返回结果
        return Response(ser.data)


class BookView(APIView):
    """获取单一, 更新, 删除"""
    def get(self, request: Request, pk):
        """获取单个书籍"""
        book = BookInfo.objects.get(id=pk)
        ser = BookSerializer(book)
        return Response(ser.data)

    def put(self, request: Request, pk):
        """更新单个书籍"""
        # 接收参数
        json_dict = request.data
        # 验证参数
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return Response({'error': '错误信息'}, status=404)
        ser = BookSerializer(book, data=json_dict)
        if not ser.is_valid():
            return Response(ser.errors)
        # 更新参数
        ser.save()
        # 返回结果
        return Response(ser.data)