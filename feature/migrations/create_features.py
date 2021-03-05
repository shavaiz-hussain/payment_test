from django.db import migrations
from feature.models import Features


class Migration(migrations.Migration):

    def seed_data(apps, schema_editor):
        features = [
            {'name': 'Feature1'},
            {'name': 'Feature2'},
            {'name': 'Feature3'},
            {'name': 'Feature4'},
            {'name': 'Feature5'},
            {'name': 'Feature6'},
            {'name': 'Feature7'},
            {'name': 'Feature8'},
            {'name': 'Feature9'},
        ]
        for feature in features:
            Features.objects.get_or_create(name=feature['name'])



    dependencies = [
        ('feature', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
