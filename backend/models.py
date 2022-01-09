from django.db import models

# Create your models here.
class APIS(models.Model):
  iframes = models.TextField()
  Title = models.TextField()
  Description = models.TextField()