# Generated by Django 4.1.6 on 2023-02-18 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_paciente_enfermedad_paciente_tipo_lesion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sintomas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10)),
                ('lesion_id', models.CharField(max_length=1)),
                ('temperatura', models.CharField(max_length=1)),
                ('edad', models.CharField(max_length=1)),
                ('dolor_cabeza', models.CharField(max_length=1)),
                ('conjuntivitis', models.CharField(max_length=1)),
                ('malestar_general', models.CharField(max_length=1)),
                ('ganglios_hinchados', models.CharField(max_length=1)),
                ('tos', models.CharField(max_length=1)),
                ('moqueo', models.CharField(max_length=1)),
                ('dolor_garganta', models.CharField(max_length=1)),
                ('diarrea', models.CharField(max_length=1)),
                ('vomito', models.CharField(max_length=1)),
                ('nauseasinfec_oid', models.CharField(max_length=1)),
                ('convulsion', models.CharField(max_length=1)),
                ('comezon', models.CharField(max_length=1)),
                ('perdida_apetito', models.CharField(max_length=1)),
                ('dolor_tragar', models.CharField(max_length=1)),
                ('hinchazon', models.CharField(max_length=1)),
                ('hinchazon_boca', models.CharField(max_length=1)),
                ('dolor_abdominal', models.CharField(max_length=1)),
                ('escalofrio', models.CharField(max_length=1)),
                ('perdida_gusto', models.CharField(max_length=1)),
                ('dolor_dentadura', models.CharField(max_length=1)),
                ('cara', models.CharField(max_length=1)),
                ('torso', models.CharField(max_length=1)),
                ('cabeza', models.CharField(max_length=1)),
                ('extremidades_superiores', models.CharField(max_length=1)),
                ('extremidades_inferiores', models.CharField(max_length=1)),
                ('genitales', models.CharField(max_length=1)),
                ('manos', models.CharField(max_length=1)),
                ('boca', models.CharField(max_length=1)),
                ('pies', models.CharField(max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='edad',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
