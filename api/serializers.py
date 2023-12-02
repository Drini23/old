from rest_framework import serializers
from albania.models import City, Attraction
"""
class CitySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)


    """
#KETU DO PERDORIM MODELSERIALIZERS

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'description']

class AttractionSerailze(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = ['name', 'description', 'city']






