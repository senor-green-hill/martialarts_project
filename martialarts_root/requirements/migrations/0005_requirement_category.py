# Generated by Django 3.0.8 on 2020-10-12 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requirements', '0004_auto_20201011_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='requirements.Category'),
        ),
    ]