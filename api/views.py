import requests
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from albania.models import City, Attraction
from .serializers import CitySerializer, AttractionSerailze



# Create your views here.

class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['id']
    search_fields = ['name']
    ordering_fields = ['id']


    def get_serializer_context(self):
        return {'request': self.request}

    def delete(self, request, id):
        city = get_object_or_404(City, pk=id)
        if city.description is not None:
            return Response({'error': 'City can not be deleted!!'})
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AttractionViewSet(ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerailze

    def get_serializer_context(self):
        return {'request': self.request}


"""
@api_view() # me kete funksion na shfaqet nje object dhe te dhenat e tij qe i kemi shkruajtur se serializer.py { http://127.0.0.1:8000/api/city/2/ }
def home(request, id):
    city = get_object_or_404(City, pk=id)
    serializer = CitySerializer(city)
    return Response(serializer.data)

#DO TE KRIJOJM NJE FUNKSRION QE TE NA SHFAQEN TE GJITHA OBJECTET QE KEMI JO VETEM 1 ME TE DHENATE PRESONALE .

@api_view()
def city_list(request):
    queryset = City.objects.all()
    serializer = CitySerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def city_detail(request, pk):
    queryset= City.objects.get(pk=pk)
    serializer = CitySerializer(queryset)
    return Response(serializer.data) """
