from rest_framework import generics, filters, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from apps.books.models import Book
from apps.books.serializers import BookSerializer
from .permissions import BookViewPermission


class BookList(generics.ListAPIView):
    """
    List all books stored in the library
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['genre', 'author', 'publisher']
    search_fields = ['title', 'author', 'publisher']
    ordering_fields = ['pub_date', 'created', 'title', 'author']

class BookAdd(generics.CreateAPIView):
    """
    Add a new book to the library
    """
    permission_classes = [BookViewPermission]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [BookViewPermission]


