from django.contrib import admin
from .models import Horaire,Absence,Poin

# Register your models here.
admin.site.register(Horaire,Absence)