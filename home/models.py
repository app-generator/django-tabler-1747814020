# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    charfielduser = models.CharField(max_length=255, null=True, blank=True)
    textfielduser = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Product(models.Model):

    #__Product_FIELDS__
    charfield = models.CharField(max_length=255, null=True, blank=True)
    textfield = models.TextField(max_length=255, null=True, blank=True)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Model2(models.Model):

    #__Model2_FIELDS__
    datefield = models.DateTimeField(blank=True, null=True, default=timezone.now)
    intergerfield = models.IntegerField(null=True, blank=True)

    #__Model2_FIELDS__END

    class Meta:
        verbose_name        = _("Model2")
        verbose_name_plural = _("Model2")



#__MODELS__END
