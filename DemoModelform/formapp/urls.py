from django.urls import path
from.import views
urlpatterns = [
  
    path('',views.home,name='home'),
    path('add',views.addcustomer,name='add'),
    path('update/<int:cid>',views.updateform,name='update')
]