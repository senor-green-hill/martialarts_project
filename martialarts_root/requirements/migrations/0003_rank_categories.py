# Generated by Django 3.0.8 on 2020-10-07 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requirements', '0002_auto_20201007_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='categories',
            field=models.ManyToManyField(to='requirements.Category'),
        ),
    ]