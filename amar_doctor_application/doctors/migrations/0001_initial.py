# Generated by Django 3.1.7 on 2021-04-20 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0002_doctor_request_patient_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=50, null=True)),
                ('take_time', models.CharField(max_length=50, null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.doctor_request')),
            ],
        ),
    ]