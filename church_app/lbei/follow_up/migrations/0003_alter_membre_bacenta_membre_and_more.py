# Generated by Django 4.1 on 2022-08-13 00:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('follow_up', '0002_bacenta_leader_bacenta_basonta_leader_basonta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membre',
            name='bacenta_membre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bacentas', to='follow_up.bacenta'),
        ),
        migrations.AlterField(
            model_name='membre',
            name='basonta_membre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='basontas', to='follow_up.basonta'),
        ),
        migrations.AlterField(
            model_name='membre',
            name='date_ajout_membre',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
