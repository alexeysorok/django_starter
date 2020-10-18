from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index-view"),
    path("articles/2003/", views.special_case_2003),
    path("articles/<int:year>/", views.year_archive),
]
