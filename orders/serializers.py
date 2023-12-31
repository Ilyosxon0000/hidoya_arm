from rest_framework import serializers
from . import models

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"

    def get_user(self,obj):
        user=obj.user
        data={
            "id": user.id,
            "first_name": user.first_name,
            "last_name":user.last_name,
            "middle_name":user.middle_name,
            "course": user.course.title if user.course else None,
            "user_type": user.user_type
        }
        return data
    
    def get_book(self,obj):
        book=obj.book
        data={
            "id": book.id,
            "title": book.title,
            "code_number": book.code_number,
        }
        return data

    def __init__(self, *args, **kwargs):
        from books.serializers import BookSerializer
        super(OrderSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request", None)
        if request and request.method == "GET":
            self.fields['user'] = serializers.SerializerMethodField("get_user")
            self.fields['book'] = serializers.SerializerMethodField("get_book")


