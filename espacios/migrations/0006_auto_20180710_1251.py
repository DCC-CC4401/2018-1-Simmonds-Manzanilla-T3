# Generated by Django 2.0.3 on 2018-07-10 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0005_auto_20180709_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservaespacio',
            name='estado',
            field=models.CharField(choices=[('PEN', 'Pendiente'), ('ACP', 'Aceptada'), ('RCH', 'Rechazada'), ('TER', 'Terminada')], default='PEN', max_length=3),
        ),
    ]