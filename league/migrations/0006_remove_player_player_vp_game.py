# Generated by Django 5.1.1 on 2024-09-30 10:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0005_rename_user_id_player_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='player_vp',
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_vp', models.PositiveIntegerField(default=0)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.player')),
            ],
        ),
    ]
