from django.db import migrations
from core.models import User


class Migration(migrations.Migration):

    def seed_data(apps, schema_editor):
        user = User(email='test@test.com',
                    is_staff=True,
                    is_superuser=True,
                    )
        user.set_password('test123')
        user.save()

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
