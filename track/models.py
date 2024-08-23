# from django.db import models
# from firebase_admin import firestore
# # Create your models here.
#
# class Pantry(models.Model):
#     Item_name=models.CharField(max_length=10)
#     Quantity=models.IntegerField()
#     Expiration_date=models.DateField()
#     Image=models.ImageField(upload_to='images/')
#
# import django_firebase_orm
# from django_firebase_orm import models
from django.db import models
class Data(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    Manufacturing_date = models.DateField()
    Expiration_date = models.DateField()
