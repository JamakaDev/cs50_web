from django.urls import path

from . import views

app_name = 'encyclopedia'
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("create", views.create, name="create"),
    path("random", views.random, name="random"),
    path("edit/<str:name>", views.edit, name='edit'),
    
]
