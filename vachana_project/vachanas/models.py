from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from authors.models import Author





class Vachana(models.Model):
    # Unique ID for each Vachana
    id = models.AutoField(primary_key=True)
    # The author of the Vachana (ForeignKey to Author)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="vachanas_written", null=True, blank=True)
    # User who submitted the Vachana (ForeignKey to User)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="submitted_vachanas")
    # Category of Vachana (e.g., love, spirituality, etc.)
    category = models.CharField(max_length=100)
    # The actual content of the Vachana
    content = models.TextField()
    # Count of likes given by other users (many-to-many relationship can be implemented for individual likes)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_vachanas", blank=True)
    
    def __str__(self):
        return f"Vachana by {self.author.name} in {self.category}"

    # Method to get total number of likes
    def total_likes(self):
        return self.likes.count()