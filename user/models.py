from email.policy import default
from shutil import register_unpack_format
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('name', 'admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError("superuser must have is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("superuser must have is_superuser=True")

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_super_user = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class AddressGlobal(models.Model):
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.address} - {self.city} - {self.state}'
    


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, related_name="user_profile", on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="profile_pics")
    address_info = models.ForeignKey(
        AddressGlobal, related_name='user_address', null=True, on_delete=models.SET_NULL
    )
    dob = models.DateField()
    
    def __str__(self):
        return self.user.email




