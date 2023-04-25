from django.db import models

class IceCreamOrder(models.Model):
    FLAVOR_CHOCOLATE = 'ch'
    FLAVOR_VANILLA = 'vn'
    FLAVOR_STRAWBERRY = 'st'
    FLAVOR_CHUNKY_MUNKY = 'cm'

    FLAVOR_CHOICES = (
        (FLAVOR_CHOCOLATE, 'Chocolate'),
        (FLAVOR_VANILLA, 'Vanilla'),
        (FLAVOR_VANILLA, 'VANILLA'),
        (FLAVOR_CHUNKY_MUNKY, 'Chunky Munky')
    )

    flavor = models.CharField(max_length=2, choices=FLAVOR_CHOICES)

    def __str__(self) -> str:
        return self.flavor
    
    # To set up briefly run these commands in shell
    """
        from orders.models import IceCreamOrder
        IceCreamOrder.objects.filter(flavor=IceCreamOrder.FLAVOR VANILLA)
        #Result will be
    """

    
