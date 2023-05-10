from django.urls import path
from flavor.api import views

urlpatterns = [
    path(
        route='api/', 
        view=views.FlavorListCreateAPIView.as_view(), 
        name='flavor_rest_api'
    ), # as /flavors/api/
    path(
        route='api/<uuid:uuid>/', 
        view=views.FlavorRetrieveUpdateDestroyAPIView.as_view(), 
        name='flavor_rest_api'
    )  # as /flavors/api/:uuid/
]


