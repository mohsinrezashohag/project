# Generated by Django 3.1.2 on 2021-04-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_auto_20210418_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(choices=[('Neurology', 'Neurology'), ('Urology', 'Urology'), ('Dentist', 'Dentist'), ('Orthopedic', 'Orthopedic'), ('Cardiologist', 'Cardiologist')], max_length=200, null=True),
        ),
    ]
