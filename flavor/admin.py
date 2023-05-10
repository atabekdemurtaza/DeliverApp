from django.contrib import admin
from .models import Flavor

@admin.register(Flavor)
class FlavorAdmin(admin.ModelAdmin):
    pass
