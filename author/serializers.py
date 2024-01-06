from rest_framework import serializers
from .models import Author,Book

class AutherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author=AutherSerializer
    class Meta:
        model = Book
        fields = '__all__'
        depth=2

