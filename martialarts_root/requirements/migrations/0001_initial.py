# Generated by Django 3.0.8 on 2020-09-28 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('position', models.IntegerField()),
                ('video_url', models.CharField(max_length=20)),
                ('desc', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('position', models.IntegerField()),
                ('eligibility', models.TextField(blank=True)),
                ('category', models.ManyToManyField(to='requirements.Category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='requirement',
            field=models.ManyToManyField(to='requirements.Requirement'),
        ),
    ]
