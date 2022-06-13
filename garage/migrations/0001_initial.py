# Generated by Django 4.0.5 on 2022-06-13 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flotte', '0004_alter_affectation_chauffeur_alter_affectation_etat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PieceRechangeGarage',
            fields=[
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=25, null=True)),
                ('code_casier', models.CharField(max_length=25, null=True)),
                ('famille', models.CharField(max_length=25, null=True)),
                ('categorie', models.CharField(max_length=25, null=True)),
                ('unite', models.CharField(max_length=25, null=True)),
                ('prix', models.IntegerField(null=True)),
                ('nombre', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlanEntretienGarage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(max_length=25, null=True)),
                ('type', models.CharField(max_length=25, null=True)),
                ('frequence', models.IntegerField(null=True)),
                ('unite', models.CharField(max_length=25, null=True)),
                ('vehicule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plan_vehicule_garage', to='flotte.vehicule')),
            ],
        ),
        migrations.CreateModel(
            name='InterventionGarage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField(null=True)),
                ('date_fin', models.DateField(null=True)),
                ('objet', models.CharField(max_length=25, null=True)),
                ('entreprise', models.CharField(max_length=25, null=True)),
                ('montant_mo_ht', models.IntegerField(null=True)),
                ('montant_pieces_ht', models.IntegerField(null=True)),
                ('montant_total_ht', models.IntegerField(null=True)),
                ('collaborateur', models.CharField(max_length=25, null=True)),
                ('vehicule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='intervention_vehicule_garage', to='flotte.vehicule')),
            ],
        ),
        migrations.CreateModel(
            name='DemandeInterventionGarage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_demande', models.DateField(null=True)),
                ('type', models.CharField(max_length=25, null=True)),
                ('description', models.TextField(max_length=255, null=True)),
                ('etat', models.BooleanField(null=True)),
                ('vehicule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='demande_vehicule_garage', to='flotte.vehicule')),
            ],
        ),
    ]
