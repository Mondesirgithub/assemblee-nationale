# Generated by Django 4.2.1 on 2023-05-17 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comptes', '0008_depute_delete_utilisateur'),
    ]

    operations = [
        migrations.AddField(
            model_name='depute',
            name='num_post',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
