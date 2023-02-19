# Generated by Django 4.1.6 on 2023-02-11 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_paciente_cedula'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='enfermedad',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='tipo_lesion',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]