from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    phone_no = PhoneNumberField(region='PL', max_length=15)
    group = models.CharField(max_length=20)

    def __str__(self):
        return "%s - %s %s" % (self.group, self.first_name, self.last_name)

    class Meta:
        ordering = ['group']
