from rest_framework import serializers
from .models import Book, GENRE_CHOICES


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publisher', 'genre', 'description', 'pub_date',
                  'created', 'updated', 'borrowed', 'pages', 'user']

    def create(self, validated_data):
        """
        Create and return a new "Book" instance, given the validated data.
        """
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return a new "Book" instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.description = validated_data.get('description', instance.description)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.pages = validated_data.get('pages', instance.pages)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance
