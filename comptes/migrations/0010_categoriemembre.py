# Generated by Django 4.2.1 on 2023-05-17 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comptes', '0009_depute_num_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='categorieMembre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
    ]
