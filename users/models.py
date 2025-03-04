from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    password = models.CharField(max_length=128)
    image = models.ImageField(upload_to='image/')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def str(self):
        return self.email

    def set_password(self, raw_password):
        """ Hash the password before saving """
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """ Check the password hash """
        return check_password(raw_password, self.password)


class ToDo(models.Model):
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('in_progress', 'In Progress'), ('Done', 'Done')])

    def __str__(self):
        return self.description
