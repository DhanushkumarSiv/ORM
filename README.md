# Ex02 Django ORM Web Application
## Date: 28-10-2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP 
![alt text](<web development.png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py

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

admin.py

from django.contrib import admin
from.models import Bankloan,BankloanAdmin
admin.site.register(Bankloan,BankloanAdmin)
```




## OUTPUT

![alt text](<Screenshot (1).png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
