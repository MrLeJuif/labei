# Generated by Django 4.1 on 2022-08-14 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('follow_up', '0006_branche'),
    ]

    operations = [
        migrations.AddField(
            model_name='membre',
            name='branche_membre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='branches', to='follow_up.branche'),
        ),
    ]
