# Generated by Django 2.1.3 on 2018-11-27 21:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('resume', '0005_auto_20181127_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationexperience',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='resume.Location'),
        ),
        migrations.AlterField(
            model_name='volunteerexperience',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='resume.Location'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='resume.Location'),
        ),
    ]
