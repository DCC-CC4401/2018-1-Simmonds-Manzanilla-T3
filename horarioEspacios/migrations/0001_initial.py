# Generated by Django 2.0.3 on 2018-07-05 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('even_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('event_type', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]