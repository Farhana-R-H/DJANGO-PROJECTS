from django.db import models

class Customer(models.Model):
    firstname=models.CharField(max_length=20,default="firstname",verbose_name="name")
    lastname=models.CharField(max_length=20,default="lastname",verbose_name="surname",blank=True)
    address=models.CharField(max_length=50)
    phone=models.BigIntegerField(default=0,verbose_name="phone number",unique=True)

    def __str__(self):
        return self.firstname
    class Meta:
        db_table="formapp_Customer"

# Create your models here.
