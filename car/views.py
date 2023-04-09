from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render

from django.views import generic

from car.models import Car
from car.serializers import CarSerializers

class CarAPIView(ListAPIView):
    queryset = Car.objects.all() #SELECT * FROM cars_car;
    serializer_class = CarSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['license_plate', ]

class CarCreateAPIView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers

class CarUpdateAPIView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers

class CarDestroyAPIView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers