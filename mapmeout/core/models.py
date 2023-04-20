from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import (
    Model,
    TextField,
    BooleanField,
    EmailField,
    CharField,
    JSONField,
    FloatField,
    ForeignKey,
    IntegerField,
    CASCADE,
)

import random
from django.core import serializers

# from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from .managers import CustomUserManager


# Create your models here.


def generate_user_id():
    """Generates a 10 digit alphanumeric unique key"""
    user_id = "".join(
        [random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVXYZ") for i in range(10)]
    )
    return user_id


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user Model --> stores user information in respective fields
    """

    user_id = CharField(max_length=10, default=generate_user_id, unique=True, null=True)
    email = EmailField("email address", unique=True)
    first_name = CharField(max_length=100, null=True, blank=True)
    last_name = CharField(max_length=100, null=True, blank=True)
    mobile_number = CharField(max_length=12, unique=True)
    password = CharField(max_length=200)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=True)
    created_date = CreationDateTimeField(null=True)
    updated_date = ModificationDateTimeField(null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)


class Volunteer(Model):
    """
    Volunteer()--> store all the details of a volunteer
    """

    user = ForeignKey(CustomUser, on_delete=CASCADE)
    pan_no = CharField(max_length=14, unique=True)
    country = CharField(max_length=50)
    state = TextField(max_length=50)
    city = TextField(max_length=50)
    apartment_add = CharField(max_length=200, blank=True, null=True)


class Rewards(Model):
    Wallet_id = CharField(max_length=200, unique=True)
    wallet_total = FloatField(max_length=10, blank=True, null=True)
    transaction_log = JSONField(blank=True, null=True)
    is_volunteer = BooleanField()
