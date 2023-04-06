from django.db import models
from library_management.settings import AUTH_USER_MODEL
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
    publisher = models.CharField(max_length=100, blank=True)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=100)
    description = models.TextField(null=True, blank=True)
    pub_date = models.DateField()
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(blank=True)
    borrowed = models.DateTimeField(null=True, blank=True)
    pages = models.IntegerField(null=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "%s - %s" % (self.author, self.title)

    class Meta:
        ordering = ["author"]

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Book, self).save(*args, **kwargs)
