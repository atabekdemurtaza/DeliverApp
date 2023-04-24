from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('', include('scoops.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]

