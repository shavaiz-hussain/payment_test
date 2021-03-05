from django.db import migrations
from charge.models import Plan


class Migration(migrations.Migration):

    def seed_data(apps, schema_editor):
        plans = [
            {'name': 'Bronze', 'price': 10.00},
            {'name': 'Gold', 'price': 20.00},
            {'name': 'Platinum', 'price': 30.00}
        ]
        for plan in plans:
            Plan.objects.get_or_create(name=plan['name'], price=plan['price'])

    dependencies = [
        ('charge', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
