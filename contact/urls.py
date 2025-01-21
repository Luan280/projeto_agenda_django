from django.urls import path
from contact import views

app_name = "contact" # NAME_SPACE

urlpatterns = [
    path('', views.index, name="index"),
]