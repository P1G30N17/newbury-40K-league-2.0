# Generated by Django 5.1.1 on 2024-09-30 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0004_alter_player_player_vp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='user_id',
            new_name='user',
        ),
    ]
