from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    age=models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="Employees"
    
# The __str__ method just tells Django what to print 
#  when it needs to print out an instance of any model    

























#Field Types in Django
# IntegerField() ,
# DecimalField(max_digits=3,decimal_places=2)         
# BigIntegerField()
# EmailField()
# DateField()
# DateTimeField()
# TextField()
# ImageField()





