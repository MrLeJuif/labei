# Generated by Django 4.1 on 2022-08-12 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bacenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_bacenta', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Basonta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_basonta', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_role', models.CharField(max_length=80, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_membre', models.CharField(max_length=256)),
                ('prenom_membre', models.CharField(max_length=256)),
                ('numero_membre', models.CharField(max_length=256)),
                ('adresse_membre', models.CharField(max_length=256)),
                ('bapteme_esprit', models.BooleanField()),
                ('bapteme_eau', models.BooleanField()),
                ('date_ajout_membre', models.DateField()),
                ('bacenta_membre', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='follow_up.bacenta')),
                ('basonta_membre', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='follow_up.basonta')),
                ('role_membre', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='follow_up.role')),
            ],
        ),
    ]
