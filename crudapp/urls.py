from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('new/', views.new, name="new"),
    path('postcreate/', views.postcreate, name="postcreate"),
    path('detail/<int:post_id>', views.detail, name="detail"),
    path('edit/', views.edit, name="edit"),
    path('postupdate/<int:post_id>', views.postupdate, name="postupdate"),
    path('postdelete/<int:post_id>', views.postdelete, name="postdelete"),
]
