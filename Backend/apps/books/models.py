from django.db import models
from apps.users.models import User
from django.utils import timezone

GENRE_CHOICES = sorted([("SF", "Sci-Fi"),
                        ("FA", "Fantastyka"),
                        ("RB", "Reportaż i Biografia"),
                        ("LE", "Lektura"),
                        ("KT", "Kryminał i Thriller"),
                        ("RO", "Romans"),
                        ("HI", "Historyczne"),
                        ])


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=100)
    description = models.TextField(null=True)
    pub_date = models.DateField(null=True)
    created = models.DateField(editable=False)
    updated = models.DateField()
    borrowed = models.DateField(null=True)
    pages = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "%s - %s" % (self.author, self.title)

    class Meta:
        ordering = ["author"]

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Book, self).save(*args, **kwargs)

