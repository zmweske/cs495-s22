# Generated by Django 4.0.3 on 2022-04-29 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0003_solution_solved'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='fixed',
            field=models.BooleanField(default=False),
        ),
    ]
