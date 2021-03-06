# Generated by Django 3.0.2 on 2021-06-21 13:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('kilimo_app', '0004_auto_20210621_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=54, null=True)),
                ('admission', models.CharField(blank=True, max_length=54, null=True)),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kilimo_app.ClassStreams')),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
