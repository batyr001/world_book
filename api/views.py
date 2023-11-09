from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework import viewsets
from .serializers import BookSerializer,GenreSerializer,LanguageSerializer,PublisherSerializer
from catalog.models import Book,Genre,Language,Publisher  

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]
   
class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language .objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.IsAuthenticated]    
 
class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [permissions.IsAuthenticated]