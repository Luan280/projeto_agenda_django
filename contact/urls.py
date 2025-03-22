from django.urls import path
from contact import views

app_name = "contact" # NAME_SPACE

urlpatterns = [
    path('<int:contact_id>/', views.contact, name="contact"),
    path('search/', views.search, name="search"),
    path('', views.index, name="index"),
]