from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title=models.CharField(max_length=25)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)  
    price=models.IntegerField()
    published_date=models.DateField(null=True,blank=True) 

    def __str__(self):
        return f"{self.title} by {self.author}" 

# Create your models here.
