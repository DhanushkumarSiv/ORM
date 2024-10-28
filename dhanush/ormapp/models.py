

from django.db import models
from django.contrib import admin
class Bankloan (models.Model):
    acc_no = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    amount = models.IntegerField()
    ifsc_code = models.IntegerField()


class BankloanAdmin(admin.ModelAdmin):
    list_display = ('acc_no','name','age','amount','ifsc_code')






