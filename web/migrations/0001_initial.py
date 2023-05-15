# Generated by Django 4.2.1 on 2023-05-15 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, verbose_name='Nom de la categorie')),
                ('icone', models.FileField(blank=True, null=True, upload_to='commissions/icones/', verbose_name='Icone de la categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50, verbose_name="Titre de l'article")),
                ('description', models.TextField(verbose_name="Description de l'article")),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categorie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='web.categorie')),
            ],
        ),
    ]
