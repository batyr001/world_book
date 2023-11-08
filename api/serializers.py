from rest_framework import serializers
from catalog.models import Book

class BookSerializer(serializers.ModelSerializer):
    # publisher = serializers.ReadOnlyField()
    # author = serializers.ReadOnlyField()
    
    class Meta:
        model = Book
        fields= "__all__"
        