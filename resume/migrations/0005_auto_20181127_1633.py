# Generated by Django 2.1.3 on 2018-11-27 21:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('resume', '0004_auto_20181127_1609'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='computerskill',
            options={'ordering': ('proficiency',), 'verbose_name': 'Computer Skill',
                     'verbose_name_plural': 'Computer Skills'},
        ),
        migrations.AlterField(
            model_name='educationexperience',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='volunteerexperience',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]