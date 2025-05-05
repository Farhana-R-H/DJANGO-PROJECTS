from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    description=models.TextField()
    image=models.ImageField(upload_to="images",null=True)


    def __str__(self):
        return self.name

# Create your models here.
