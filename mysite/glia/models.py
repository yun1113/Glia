from django.db import models

# Create your models here.
class Display(models.Model):
    num = models.BigIntegerField()
    title = models.CharField(max_length=200)
    def __str__(self):
            return self.title
