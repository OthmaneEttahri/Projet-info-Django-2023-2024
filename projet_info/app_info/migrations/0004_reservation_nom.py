# Generated by Django 4.1.6 on 2024-01-30 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_info', '0003_alter_reservation_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='nom',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
