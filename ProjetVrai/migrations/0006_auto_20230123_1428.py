# Generated by Django 3.1.2 on 2023-01-23 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjetVrai', '0005_auto_20230123_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiel',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
