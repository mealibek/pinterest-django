from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class ProfileManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, **other_fields):
        if not email:
            raise ValueError('Email must be set')

        if not password:
            raise ValueError('Password must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name, **other_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, first_name, last_name, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, first_name, last_name, **other_fields)


class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email address', unique=True)
    profile_image = models.CharField(
        "Profile Image", max_length=300, null=True, blank=True)
    first_name = models.CharField('First name', max_length=30)
    last_name = models.CharField('Last name', max_length=30)
    is_active = models.BooleanField('Active mode', default=True)
    is_superuser = models.BooleanField('Superuser mode', default=False)
    is_staff = models.BooleanField('Staff mode', default=False)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    modified_at = models.DateTimeField('Modified at', auto_now=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = ProfileManager()

    def __str__(self) -> str:
        return self.email

    class Meta:
        db_table = 'profiles'
        verbose_name_plural = 'Profiles'
