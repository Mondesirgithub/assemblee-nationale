# Generated by Django 4.2.1 on 2023-05-18 11:26

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('comptes', '0014_alter_depute_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depute',
            name='photo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default=None, force_format=None, keep_meta=True, null=True, quality=100, scale=None, size=[60, 80], upload_to='Deputes/photos/'),
        ),
    ]