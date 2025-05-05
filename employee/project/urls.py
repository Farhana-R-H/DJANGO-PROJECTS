from django.urls import path
from.import views
urlpatterns=[
    path("",views.home,name="home"),
    path("addition",views.addemployee),
    path("dis",views.display),
    path("update",views.update_employee),
    path("delete",views.delete_employee),
    path("viewemp/<int:eid>",views.singleempview),
    path("login",views.loginview),
    path("logout",views.logout_view),
    path('accounts/signup/',views.sign_up,name='register'),
    path("reset",views.reset_password,name="reset"),
    path("passwordreset",views.new_password)

]




