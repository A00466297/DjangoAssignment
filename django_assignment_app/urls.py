from django.urls import path
from . import views

urlpatterns= [
    path("home/", views.home),
    path("hotel/", views.hotel_list),
    path("hotel/<str:pk>", views.hotels_details),
]