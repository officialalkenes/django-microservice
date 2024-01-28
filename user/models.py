from typing import Optional, Set
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.core.validators import MinLengthValidator

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12, validators=[MinLengthValidator(11)])
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_("Date Joined"), auto_now_add=True)
    last_login = models.DateTimeField(_("Last Login Date"), auto_now=True)
    verified = models.BooleanField(
        _("email_verify"),
        default=False,
        help_text=_("Designates whether this user's email has been Verified. "),
    )

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number"]

    objects = UserManager()

    def __str__(self) -> str:
        return f"{self.email}"


class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, db_index=True, null=True, blank=True)
    login = models.DateTimeField(auto_now_add=True)
    logout = models.DateTimeField(null=True, default=None)


class LoginAttempt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login_attempts = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "user: {}, attempts: {}".format(self.user.email, self.login_attempts)
