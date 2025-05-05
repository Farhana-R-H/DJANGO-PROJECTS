from django.urls import path
from.import views
urlpatterns=[
    path("",views.home),
    path("show",views.display)

]