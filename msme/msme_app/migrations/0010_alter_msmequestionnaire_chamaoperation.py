# Generated by Django 3.2 on 2024-04-08 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msme_app', '0009_auto_20240405_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msmequestionnaire',
            name='chamaOperation',
            field=models.CharField(choices=[('0-1', '0-1'), ('1-2', '1-2'), ('above 2', 'above 2')], max_length=20),
        ),
    ]
