from django.db import models

# Create your models here.


class Portfolio(models.Model):
    title = models.CharField(max_length=100, blank=False)
    short_description = models.TextField(max_length=540, blank=False)
    image = models.ImageField(upload_to='images/', blank=False)
    live_page = models.URLField(max_length=200, blank=True)
    github_repo = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    detailed_description = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.title
