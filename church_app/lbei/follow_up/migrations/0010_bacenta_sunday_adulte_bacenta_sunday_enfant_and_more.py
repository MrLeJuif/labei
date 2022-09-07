# Generated by Django 4.1 on 2022-08-15 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow_up', '0009_alter_membre_numero_membre_basonta_rapport_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bacenta_sunday',
            name='adulte',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bacenta_sunday',
            name='enfant',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bacenta_sunday',
            name='nouveau',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bacenta_sunday',
            name='offrande',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bacenta_sunday',
            name='transport',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bacenta_week',
            name='adulte',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bacenta_week',
            name='enfant',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bacenta_week',
            name='nee_de_nouveau',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bacenta_week',
            name='nouveau',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basonta_rapport',
            name='adulte',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basonta_rapport',
            name='enfant',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basonta_rapport',
            name='nouveau',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bacenta_week',
            name='offrande',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='basonta_rapport',
            name='offrande',
            field=models.PositiveIntegerField(default=0),
        ),
    ]