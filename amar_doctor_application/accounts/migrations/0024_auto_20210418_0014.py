# Generated by Django 3.1.2 on 2021-04-17 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20210418_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(choices=[('Neurology', 'Neurology'), ('Orthopedic', 'Orthopedic'), ('Cardiologist', 'Cardiologist'), ('Urology', 'Urology'), ('Dentist', 'Dentist')], max_length=200, null=True),
        ),
    ]
