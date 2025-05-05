from django.shortcuts import render
from.models import Author,Book

def book_by_author(request,author_id):
    author=Author.objects.get(id=author_id)
    books=Book.objects.filter(author=author)
    context={
        "author" : author,
        "books" : books,
    }
    return render(request,"book.html",context)
# Create your views here.
