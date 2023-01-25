from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Branch(models.Model):
    branch_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.branch_name}'