# Generated by Django 3.1.2 on 2021-04-18 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_auto_20210418_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(choices=[('Urology', 'Urology'), ('Cardiologist', 'Cardiologist'), ('Orthopedic', 'Orthopedic'), ('Dentist', 'Dentist'), ('Neurology', 'Neurology')], max_length=200, null=True),
        ),
    ]
