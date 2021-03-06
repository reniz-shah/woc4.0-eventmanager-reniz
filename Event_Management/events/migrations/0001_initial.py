# Generated by Django 4.0.1 on 2022-01-21 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('venue', models.CharField(max_length=120)),
                ('fromDate', models.DateTimeField()),
                ('toDate', models.DateTimeField()),
                ('Deadline', models.DateTimeField()),
                ('hostemail', models.CharField(max_length=50)),
                ('hostpassword', models.CharField(max_length=50)),
            ],
        ),
    ]
