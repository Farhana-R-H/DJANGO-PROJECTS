from django.contrib import admin
from.models import Book,Author


class BookAdmin(admin.ModelAdmin):
    list_display=["id","title","author","price","published_date"]
    ordering=("price",)

class AuthorAdmin(admin.ModelAdmin):
    list_display=["id","name"]


admin.site.site_header="Book Administration"
admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
