from .serializers import FlavorSerializer
from ..models import Flavor
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class FlavorListCreateAPIView(ListCreateAPIView):
    queryset = Flavor.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = FlavorSerializer
    lookup_field = 'uuid' # Do not use a flavor id Never Atabek!

class FlavorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Flavor.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = FlavorSerializer
    lookup_field = 'uuid' # Do not use a flavor id Never Atabek

    