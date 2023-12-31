import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.


class UserAccountManager(BaseUserManager):

    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, password, **extra_fields)


class UserAccount(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)

    email = models.EmailField(max_length=254, unique=True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    date_joined = models.DateTimeField(
        default=timezone.now, auto_now=False, auto_now_add=False)

    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    age = models.IntegerField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'date_of_birth',
    ]

    def save(self, *args, **kwargs):

        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        super(UserAccount, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.email
