from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import FlavorReview

@transaction.non_atomic_requests
def posting_flavor_status(request, pk, status):
    flavor = get_object_or_404(FlavorReview, pk=pk)
    flavor.latest_status_change_attempt = timezone.now()
    flavor.save()

    with transaction.atomic():
        # This code executes inside a transaction
        flavor.status = status
        flavor.latest_status_change_attempt = timezone.now()
        flavor.save()
        return HttpResponse('Hooray')
    
    # If the transaction fails, return the appropriate status
    return HttpResponse('Sadness', status_code=400)

