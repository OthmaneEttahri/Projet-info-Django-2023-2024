# Generated by Django 4.1.6 on 2024-01-30 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_info', '0004_reservation_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='table',
            name='nom',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
