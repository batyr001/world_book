from rest_framework import serializers
from catalog.models import Book,Genre   

class BookSerializer(serializers.ModelSerializer):
    # publisher = serializers.ReadOnlyField()
    # author = serializers.ReadOnlyField()
    
    class Meta:
        model = Book
        fields= "__all__"
        
# class GenreSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Genre        
#         fields= "__all__"
        
        