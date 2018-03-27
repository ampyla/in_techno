# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import UserManager,Group
from django.db import models
from django.forms import CheckboxSelectMultiple

class Company(models.Model):
    name = models.TextField(max_length=255)
    managers = models.ManyToManyField(Group, related_name='company_manager',blank=True)
    #managers = models.ForeignKey(Group, related_name='company_manager')
    slug = models.SlugField(verbose_name="Url компании")
    image = models.ImageField(upload_to='images//%Y/%m/%d', blank=True, null=True)

# Create your models here.
