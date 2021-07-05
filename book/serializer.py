from rest_framework import serializers


class PeopleSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    book = serializers.StringRelatedField()

class BookSerializer(serializers.Serializer):
    name = serializers.CharField()
    pub_date = serializers.DateField()
    readcount = serializers.IntegerField()
    # 返回关联的人物ID
    # peopleinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # 返回关联的人物名称
    # peopleinfo_set = serializers.StringRelatedField(read_only=True, many=True)
    # 返回自定义的人物信息
    peopleinfo_set = PeopleSerializer(many=True)