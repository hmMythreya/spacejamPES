from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.bms,name="bms"),
    path("",views.rvce,name="rvce"),
    path("",views.pes,name="pes"),
    path("",views.msrit,name="msrit")
]