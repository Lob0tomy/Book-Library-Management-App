from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    phone_no = models.IntegerField(max_length=15)
    group = models.CharField()

    def __str__(self):
        return "%s - %s %s" % (self.group, self.first_name, self.last_name)
