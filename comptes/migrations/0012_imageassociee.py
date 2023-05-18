# Generated by Django 4.2.1 on 2023-05-17 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comptes', '0011_depute_categoriemembre'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageAssociee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.ImageField(blank=True, null=True, upload_to='actualites/images/')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]