# Generated by Django 4.0.3 on 2022-03-03 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='patient_since',
            field=models.DateField(auto_now=True),
        ),
    ]
