from django.contrib import admin
from .models import IceCreamOrder
from .models import IceOrder
from .models import FlavorReview

admin.site.register(IceCreamOrder)
admin.site.register(IceOrder)
admin.site.register(FlavorReview)



