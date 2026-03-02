from django.contrib import admin
from .models import Horaire,Absence,Pointage

# Register your models here.
admin.site.register(Horaire,Absence,Pointage)