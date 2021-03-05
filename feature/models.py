from django.db import models
from charge.models import Plan
from core.utils.utils import get_random_plan
# Create your models here.


class Features(models.Model):
    name = models.CharField(max_length=255)
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, default=get_random_plan)
