from django.db import models

# Create your models here.
class color(models.Model):
    color = models.CharField(max_length=200)
    def _str_(self):
        return self.name