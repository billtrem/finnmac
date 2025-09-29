from django.db import models

class PageImage(models.Model):
    """Single image for the one-page Finn Mac site"""
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="finnmac/")

    def __str__(self):
        return self.title or "Page Image"

    class Meta:
        verbose_name = "Page Image"
        verbose_name_plural = "Page Images"
