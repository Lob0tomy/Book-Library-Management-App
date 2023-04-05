from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.books.models import Book
from apps.books.serializers import BookSerializer


class BookList(generics.ListCreateAPIView):
    """
    List all books or create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['genre', 'author', 'publisher']
    search_fields = ['title', 'author', 'publisher']
    ordering_fields = ['pub_date', 'created', 'title', 'author']


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


