from django.urls import path
from . import views, post_view


urlpatterns = [
    path("main/", views.main, name="index-view"),
    path("main/text/", views.text, name="text"),
    path("main/file/", views.file, name="file"),
    path("main/redirect/", views.redirect, name="redirect"),
    path("main/not-allowed/", views.not_allowed, name="not_allowed"),
    path("main/json/", views.json, name="json"),

    # path('class-view/', views.MyView.as_view(), name='class_view'),
    # path('class-view/text', views.MyView.as_view(), name='class_view_text'),

    path('post/', post_view.MyTemplateView.as_view(), name="post"),
    path('post/<int:number>/', post_view.post_page, name="post_list"),
]
