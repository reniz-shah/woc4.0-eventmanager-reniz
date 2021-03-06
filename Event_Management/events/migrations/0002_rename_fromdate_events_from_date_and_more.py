# Generated by Django 4.0.1 on 2022-01-21 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='fromDate',
            new_name='from_Date',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='hostemail',
            new_name='host_email',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='hostpassword',
            new_name='host_password',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='toDate',
            new_name='to_Date',
        ),
        migrations.CreateModel(
            name='participate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=18)),
                ('email_id', models.CharField(max_length=50)),
                ('registeration_type', models.CharField(choices=[('INDIVIDUAL', 'Individual'), ('GROUP', 'Group')], max_length=10)),
                ('no_of_people', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.events')),
            ],
        ),
    ]
