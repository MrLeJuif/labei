# Generated by Django 4.1 on 2022-08-14 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('follow_up', '0007_membre_branche_membre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membre',
            name='branche_membre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='branches', to='follow_up.branche'),
        ),
    ]