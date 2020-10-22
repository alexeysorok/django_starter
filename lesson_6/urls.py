from django.urls import path
from . import views

urlpatterns = [
    path('try-forms/', views.my_form, name='my_form'),


]