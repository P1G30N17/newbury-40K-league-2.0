# Generated by Django 5.1.1 on 2024-10-04 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0009_delete_updatestats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='player_vp',
        ),
    ]
