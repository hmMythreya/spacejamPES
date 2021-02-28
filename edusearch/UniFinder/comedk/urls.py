from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('/cse',views.checkCollegeCSE,name="cse"),
    path('/ece',views.checkCollegeECE,name="ece"),
]