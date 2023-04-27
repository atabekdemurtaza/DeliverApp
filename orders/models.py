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


class IceOrder(models.Model):
    class Flavors(models.TextChoices):
        CHOCOLATE = 'ch', 'Chocolate'
        VANILLA = 'vn', 'Vanilla'
        STRAWBERYY = 'st', 'Strawberry'
        CHUNKY_MUNKY = 'cm', 'Chunky Munky'
    
    flavor = models.CharField(
        max_length=2,
        choices=Flavors.choices
    )

    def __str__(self) -> str:
        return self.flavor

class FlavorReview(models.Model):
    review = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.review