from django.db import models
from uuid import uuid4
from django.utils.translation import gettext as _
from django.urls import reverse

class Flavor(models.Model):
    title = models.CharField(_('Название'), max_length=20, blank=True, null=True)
    slug = models.SlugField(_('Слаг'), default='', unique=True)
    uuid = models.UUIDField(db_index=True, default=uuid4, editable=False)
    scoops_remaining = models.IntegerField(_('Остаток'), default=0)
    createdAt = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse("flavors:detail", kwargs={"slug": self.slug})
    
    def __str__(self) -> str:
        return f'{self.title} with {self.createdAt}'

    class Meta:
        verbose_name_plural = 'Особенности'
        verbose_name = 'Особенность'
        ordering = ['-createdAt'] 
        
          
