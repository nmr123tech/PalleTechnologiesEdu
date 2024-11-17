from sys import path

from app1 import views

urlpatterns = [
path('',views.home),
path('greencolor/',views.color_home),