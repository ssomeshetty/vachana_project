from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Author(models.Model):
    # Unique author name
    name = models.CharField(max_length=200, unique=True)
    # Author's biography or other info
    information = models.TextField(verbose_name="Author Information")
    # Photo of the author
    photo = models.ImageField(upload_to='static/images/', null=True, blank=True)
    
    # Relationship: One author can have many vachanas
    vachanas = models.ForeignKey('vachanas.Vachana', on_delete=models.CASCADE, related_name='authors', null=True, blank=True)

    def __str__(self):
        return self.name