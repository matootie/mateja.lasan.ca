# Generated by Django 2.1.7 on 2019-03-29 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_coverletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='computerskill',
            name='parent_skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subskills', to='resume.ComputerSkill'),
        ),
    ]
