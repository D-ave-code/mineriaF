# Generated by Django 4.1.6 on 2023-02-18 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_nauseasinfec_oid_sintomas_infec_oid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sintomas',
            name='boca',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='cabeza',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='cara',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='comezon',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='conjuntivitis',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='convulsion',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='diarrea',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='dolor_abdominal',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='dolor_cabeza',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='dolor_dentadura',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='dolor_garganta',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='dolor_tragar',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='edad',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='escalofrio',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='extremidades_inferiores',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='extremidades_superiores',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='ganglios_hinchados',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='genitales',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='hinchazon',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='hinchazon_boca',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='infec_oid',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='lesion_id',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='malestar_general',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='manos',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='moqueo',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='nauseas',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='perdida_apetito',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='perdida_gusto',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='pies',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='torso',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='tos',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='sintomas',
            name='vomito',
            field=models.CharField(max_length=2),
        ),
    ]
