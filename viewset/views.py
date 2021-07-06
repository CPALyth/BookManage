from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from view.models import BookInfo
from view.serializer import BookSerializer

class BookView(ViewSet):
    """获取所有, 新增图书, 获取单一, 更新, 删除"""
    def list(self, request):
        """获取所有图书"""
        books = BookInfo.objects.filter(is_delete=False)
        ser = BookSerializer(books, many=True)  # 返回多个对象, 要把many设为True
        return Response(ser.data)

    def create(self, request):
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

    def retrieve(self, request, pk):
        """获取单个书籍"""
        book = BookInfo.objects.get(id=pk)
        ser = BookSerializer(book)
        return Response(ser.data)

    def update(self, request, pk):
        """更新单个书籍"""
        # 接收参数
        json_dict = request.data
        # 验证参数
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return Response({'error': '错误信息'}, status=404)
        ser = BookSerializer(book, data=json_dict)
        ser.is_valid()
        # 更新参数
        ser.save()
        # 返回结果
        return Response(ser.data)

    def othermethod(self, request, pk):
        """获取单个书籍"""
        book = BookInfo.objects.get(id=pk)
        ser = BookSerializer(book)
        return Response(ser.data)
