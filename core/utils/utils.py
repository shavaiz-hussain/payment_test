import datetime
from dateutil.relativedelta import relativedelta


def get_expire_date():
    today = datetime.date.today()
    return today + relativedelta(months=1)


def get_random_plan():
    from charge.models import Plan
    return Plan.objects.order_by('?')[0]