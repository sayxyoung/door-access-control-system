from django.db  import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def create_user(
        self,
        email,
        password = None,
        **extra_fields
    ):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_super_user(
        self,
        email,
        password,
    ):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self.db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name


class Generation(models.Model):
    user = models.ForeignKey('accounts.user', on_delete=models.CASCADE, related_name='generations')
    name = models.CharField(max_length=10)
    access_password = models.CharField(max_length=300)

    def __str__(self):
        return self.name