
from django.urls import path
from sbadmin import views
urlpatterns = [
    path("", views.index, name="index")
]
