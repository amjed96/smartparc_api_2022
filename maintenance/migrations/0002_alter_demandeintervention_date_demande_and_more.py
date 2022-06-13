# Generated by Django 4.0.5 on 2022-06-13 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flotte', '0004_alter_affectation_chauffeur_alter_affectation_etat_and_more'),
        ('maintenance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandeintervention',
            name='date_demande',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demandeintervention',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='demandeintervention',
            name='etat',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demandeintervention',
            name='type',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='demandeintervention',
            name='vehicule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='demande_vehicule', to='flotte.vehicule'),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='collaborateur',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='date_debut',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='date_fin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='entreprise',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='montant_mo_ht',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='montant_pieces_ht',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='montant_total_ht',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='objet',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='vehicule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='intervention_vehicule', to='flotte.vehicule'),
        ),
        migrations.AlterField(
            model_name='piecerechange',
            name='categorie',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='piecerechange',
            name='code_casier',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='piecerechange',
            name='famille',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='piecerechange',
            name='nom',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='piecerechange',
            name='nombre',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='piecerechange',
            name='prix',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='piecerechange',
            name='unite',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='planentretien',
            name='frequence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='planentretien',
            name='type',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='planentretien',
            name='unite',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='planentretien',
            name='vehicule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plan_vehicule', to='flotte.vehicule'),
        ),
    ]
