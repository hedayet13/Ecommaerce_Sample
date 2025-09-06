from django.db import models
class Banner(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="banners/")
    cta_label = models.CharField(max_length=50, blank=True)
    cta_url = models.URLField(blank=True)
    active = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ["ordering","id"]
    def __str__(self): return self.title
