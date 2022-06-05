# Generated by Django 4.0.5 on 2022-06-05 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('bgg_id', models.IntegerField(blank=True, null=True)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('thumbnail', models.CharField(blank=True, max_length=250, null=True)),
                ('img', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('year_published', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
