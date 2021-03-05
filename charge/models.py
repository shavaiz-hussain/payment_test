from django.db import models
from model_utils.models import TimeStampedModel
from core.models import User
from core.utils.utils import get_expire_date


class Plan(TimeStampedModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.BooleanField(default=True)


class PlanSubscription(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    plan = models.OneToOneField(Plan, on_delete=models.PROTECT)
    status = models.BooleanField(default=False)
    re_subscribe = models.BooleanField(default=True)
    expire_date = models.DateField(default=get_expire_date)
