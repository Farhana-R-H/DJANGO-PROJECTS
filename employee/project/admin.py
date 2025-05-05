from django.contrib import admin
from.models import Employee


class EmployeeAdmin(admin.ModelAdmin): 
    list_display=['id','name','address','age']   #Model class field names
    ordering = ('-name',)
    search_fields = ('name',)
    
admin.site.register(Employee,EmployeeAdmin)


