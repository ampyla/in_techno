# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
from django.forms import CheckboxSelectMultiple

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','image','slug')
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


# Register your models here.
admin.site.register(Company, CompanyAdmin)