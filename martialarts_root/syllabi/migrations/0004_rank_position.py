# Generated by Django 3.0.8 on 2020-08-11 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabi', '0003_rank_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='position',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
