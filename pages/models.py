from django.db import models
from django.urls import reverse
class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    def get_absolute_url(self): return reverse("page_detail", args=[self.slug])
    def __str__(self): return self.title
