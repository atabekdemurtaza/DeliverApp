from ..models import Flavor
from rest_framework import serializers

class FlavorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flavor
        fields = ['title','slug','uuid','scoops_remaining']


