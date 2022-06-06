# Generated by Django 4.0.5 on 2022-06-06 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default=123456789, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=123456789, max_length=25, unique=True),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Visite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('diagnostique', models.TextField(blank=True, max_length=255, null=True)),
                ('num_ordonnance', models.CharField(blank=True, max_length=25, null=True)),
                ('personnel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visites_personnel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Permis',
            fields=[
                ('reference', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
                ('personnel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permis_personnel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Passeport',
            fields=[
                ('numero', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=25, null=True)),
                ('nationalite', models.CharField(blank=True, max_length=25, null=True)),
                ('adresse_naissance', models.CharField(blank=True, max_length=25, null=True)),
                ('sexe', models.CharField(blank=True, max_length=25, null=True)),
                ('authorite_edition', models.CharField(blank=True, max_length=25, null=True)),
                ('date_edition', models.DateField(blank=True, null=True)),
                ('date_expiration', models.DateField(blank=True, null=True)),
                ('personnel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='passeport_personnel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
