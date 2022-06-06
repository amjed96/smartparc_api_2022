# Generated by Django 4.0.5 on 2022-06-06 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tiers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('reference', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('article', models.CharField(blank=True, max_length=25, null=True)),
                ('codecasier', models.CharField(blank=True, max_length=25, null=True)),
                ('dateachat', models.DateField(blank=True, null=True)),
                ('quantite', models.IntegerField(blank=True, null=True)),
                ('unite', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=25, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('numero', models.CharField(blank=True, max_length=25, null=True)),
                ('tiers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documents_tiers', to='tiers.tiers')),
            ],
        ),
        migrations.CreateModel(
            name='DemandeAchat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('article', models.CharField(blank=True, max_length=255, null=True)),
                ('nombre', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('statut', models.BooleanField(blank=True, null=True)),
                ('demandeur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personnel_demande_achat', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
