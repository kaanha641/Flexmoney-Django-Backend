# Generated by Django 5.0 on 2023-12-18 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollments',
            old_name='created_at',
            new_name='enrollment_date',
        ),
        migrations.AddField(
            model_name='enrollments',
            name='validity',
            field=models.TextField(choices=[('comlpeted', 'Completed'), ('valid', 'Valid'), ('invalid', 'Invalid')], default='invalid'),
        ),
    ]
