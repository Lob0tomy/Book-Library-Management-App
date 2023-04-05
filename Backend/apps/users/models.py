from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from .managers import AccountManager


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='email', unique=True)
    phone_no = PhoneNumberField(region='PL', max_length=15)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created = models.DateField(editable=False)
    borrowed_books = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='image', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    objects = AccountManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return "%s: %s %s" % (self.email, self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(User, self).save(*args, **kwargs)
