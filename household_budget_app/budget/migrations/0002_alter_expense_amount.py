# Generated by Django 5.0.7 on 2024-08-06 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
    ]
