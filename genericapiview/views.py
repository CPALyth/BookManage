from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from view.models import BookInfo
from view.serializer import BookSerializer

class BooksView(GenericAPIView):
    """获取所有, 新增图书"""
    queryset = BookInfo.objects.filter(is_delete=False)  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  # 指定当前类视图使用的序列化器

    def get(self, request: Request):
        """获取所有图书"""
        books = self.get_queryset()  # 获取查询集中的所有数据
        ser = self.get_serializer(books, many=True)
        return Response(ser.data)

    def post(self, request: Request):
        """新增单个图书"""
        # 1 获取数据
        json_dict = request.data
        # 2 验证数据
        ser = self.get_serializer(data=json_dict)
        ser.is_valid()
        # 3 保存数据
        ser.save()
        # 4 返回结果
        return Response(ser.data)


class BookView(GenericAPIView):
    """获取单一, 更新, 删除"""
    queryset = BookInfo.objects.filter(is_delete=False)  # 指定当前类视图使用的查询集数据
    serializer_class = BookSerializer  # 指定当前类视图使用的序列化器

    def get(self, request: Request, pk):
        """获取单个书籍"""
        book = self.get_object()
        ser = self.get_serializer(book)
        return Response(ser.data)

    def put(self, request: Request, pk):
        """更新单个书籍"""
        # 接收参数
        json_dict = request.data
        # 验证参数
        try:
            book = self.get_object()
        except:
            return Response({'error': '错误信息'}, status=404)
        ser = self.get_serializer(book, data=json_dict)
        if not ser.is_valid():
            return Response(ser.errors)
        # 更新参数
        ser.save()
        # 返回结果
        return Response(ser.data)