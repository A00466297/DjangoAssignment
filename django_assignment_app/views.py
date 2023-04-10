from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Hotels
from rest_framework.decorators import api_view
from .serializers import HotelSerializers
from rest_framework import generics
from rest_framework import filters


def home(request):
    return HttpResponse("<h1> HELLO WORLD </h1>")


@api_view(['GET', 'POST'])
def hotel_list(request):
    if request.method == 'GET':
        list_of_hotels = Hotels.objects.all()
        hotel_serializer = HotelSerializers(list_of_hotels, many=True)
        return Response(hotel_serializer.data)
    if request.method == 'POST':
        hotel_request = request.data
        serialize_request_data = HotelSerializers(data=hotel_request)
        if serialize_request_data.is_valid():
            serialize_request_data.save()
        return Response({"Message": "Added Successfully"})


@api_view(['GET', 'POST'])
def hotels_details(request, pk):
    if request.method == 'GET':
        list_of_hotels = Hotels.objects.get(id=pk)
        hotel_serializer = HotelSerializers(list_of_hotels, many=False)
        return Response(hotel_serializer.data)
