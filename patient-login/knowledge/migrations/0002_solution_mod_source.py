# Generated by Django 4.0.3 on 2022-04-07 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='mod_source',
            field=models.CharField(default='login', max_length=50),
            preserve_default=False,
        ),
    ]
