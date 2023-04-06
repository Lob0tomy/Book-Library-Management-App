from rest_framework import generics, filters, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from apps.books.models import Book
from apps.books.serializers import BookSerializer
from .permissions import BookViewPermission


# class BooksViewSet(ViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [BookViewPermission]
#
#     def list(self, request):
#         filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#         filterset_fields = ['genre', 'author', 'publisher']
#         search_fields = ['title', 'author', 'publisher']
#         ordering_fields = ['pub_date', 'created', 'title', 'author']
#         serializer = self.get_serializer(self.get_queryset(), many=True)
#         return self.get_paginated_response(self.paginate_queryset(serializer.data))
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(serializer)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)



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


