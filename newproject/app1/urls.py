from django.urls import path
from.import views
urlpatterns=[
    path("",views.home,name="home"),
    path("addition",views.add),
    path("login",views.loginview),
    path("logout",views.logout_view)

    

]