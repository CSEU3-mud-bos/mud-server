# Generated by Django 3.0.3 on 2020-03-03 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0002_auto_20200303_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='e_to',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='n_to',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='s_to',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='w_to',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
