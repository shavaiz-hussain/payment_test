import datetime
from core.utils.utils import get_expire_date
from celery import shared_task
from charge.models import PlanSubscription
from core.utils.mock_charge import mock_charge
import logging

logger = logging.getLogger(__name__)


@shared_task(name="update_subscription")
def update_subscription():
    """
    Task to update the subscription which are expiring today
    """
    today = datetime.date.today()
    update_subscriptions = PlanSubscription.objects.filter(status=True, expire_date=today, re_subscribe=True)
    # deleting the subscription which are already been unsubscribed
    PlanSubscription.objects.filter(expire_date=today, re_subscribe=False)
    for subscription in update_subscriptions:
        logger.debug(
            "The subscription {} of {} has been updated".format(
                subscription, subscription.user.email
            )
        )
        try:
            response = mock_charge()
            if response['paid'] and response['status'] == 'succeeded':
                subscription = PlanSubscription.objects.get(pk=subscription.pk)
                subscription.expire_date = get_expire_date()
                subscription.save()
            else:
                PlanSubscription.objects.filter(pk=subscription.pk).delete()
        except Exception:
            PlanSubscription.objects.filter(pk=subscription.pk).delete()
