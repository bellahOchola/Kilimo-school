# Generated by Django 3.0.2 on 2021-06-21 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilimo_app', '0003_auto_20210621_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classstreams',
            name='students_number',
            field=models.IntegerField(blank=True, max_length=54, null=True),
        ),
    ]