# Generated by Django 4.0 on 2021-12-12 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='about',
            field=models.CharField(blank=True, default=None, max_length=2083, null=True),
        ),
    ]
