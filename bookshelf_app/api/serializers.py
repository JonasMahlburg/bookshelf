from rest_framework import serializers
from bookshelf_app.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'