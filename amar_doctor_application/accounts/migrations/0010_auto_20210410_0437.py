# Generated by Django 3.1.7 on 2021-04-09 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_doctor_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_image',
            field=models.ImageField(default='d.png', upload_to='uploded_image/'),
        ),
    ]