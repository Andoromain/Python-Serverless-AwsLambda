# Generated by Django 3.1.2 on 2023-01-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjetVrai', '0004_auto_20230123_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiel',
            name='image',
            field=models.FileField(upload_to='media/'),
        ),
    ]
