from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework import viewsets
from .serializers import BookSerializer
from catalog.models import Book

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    