from django.urls import path

# now import the views.py file into this code
from . import views

urlpatterns = [
    path("list/", views.list, name="list"),
    path("detail/<int:movie_id>", views.detail, name="detail"),
]
