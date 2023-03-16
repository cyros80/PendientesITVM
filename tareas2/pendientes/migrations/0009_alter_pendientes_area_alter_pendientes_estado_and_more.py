# Generated by Django 4.0.5 on 2023-03-10 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendientes', '0008_alter_pendientes_area_alter_pendientes_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendientes',
            name='Area',
            field=models.CharField(choices=[('SubAdministrativa', 'SubAdministrativa'), ('SubAcademica', 'SubAcademica'), ('SubPlaneacion', 'SubPlaneacion')], max_length=30, verbose_name='Area'),
        ),
        migrations.AlterField(
            model_name='pendientes',
            name='estado',
            field=models.CharField(choices=[('Finalizada', 'Finalizada'), ('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso')], default='Pendiente', max_length=25, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]