# Generated by Django 4.2.4 on 2023-08-28 19:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("crash_game", "0003_bet_bound_game_player_round_round_unique_round_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Game",
        ),
    ]
