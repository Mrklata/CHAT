# Generated by Django 3.0.6 on 2020-05-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]