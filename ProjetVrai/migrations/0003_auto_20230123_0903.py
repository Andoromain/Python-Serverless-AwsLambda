# Generated by Django 3.1.2 on 2023-01-23 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjetVrai', '0002_auto_20210105_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiel',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
