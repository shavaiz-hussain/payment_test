# Generated by Django 3.1.3 on 2020-12-06 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charge', '0001_plan_allow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='allow',
        ),
    ]
