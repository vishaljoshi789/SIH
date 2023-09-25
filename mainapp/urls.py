from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('gender', views.gender, name="gender"),
    path('caste', views.caste, name="caste"),
    path('age', views.age, name="age"),
    path('region', views.region, name="region"),
    
]