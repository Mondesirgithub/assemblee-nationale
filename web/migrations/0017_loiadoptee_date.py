# Generated by Django 4.2.1 on 2023-05-18 17:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_alter_actualitevideo_lien'),
    ]

    operations = [
        migrations.AddField(
            model_name='loiadoptee',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]