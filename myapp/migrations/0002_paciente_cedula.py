# Generated by Django 4.1.6 on 2023-02-11 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='cedula',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
