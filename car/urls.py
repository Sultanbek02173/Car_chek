from django.urls import path

from . import views
from car.views import CarAPIView, CarCreateAPIView, CarUpdateAPIView, CarDestroyAPIView

urlpatterns = [
    path('cars/', CarAPIView.as_view(), name="api_cars"),
    path('cars/create', CarCreateAPIView.as_view(), name="api_cars_craete"),
    path('cars/update/<int:pk>/', CarUpdateAPIView.as_view(), name="api_cars_update"),
    path('cars/destroy/<int:pk>/', CarDestroyAPIView.as_view(), name="api_cars_update"),
]