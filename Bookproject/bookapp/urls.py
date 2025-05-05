from django.urls import path
from.import views

urlpatterns=[
    path("books_by_author/<int:author_id>",views.book_by_author)
]