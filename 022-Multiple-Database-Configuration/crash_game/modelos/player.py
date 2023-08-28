import uuid
from typing import TYPE_CHECKING

from django.db import models

from crash_game.enums import PlayerStateOption


class Player(models.Model):
    class Meta:
        db_table = "igaming_player"
        constraints = [
            models.UniqueConstraint(
                fields=["casino_id", "external_id"],
                name="unique_player",
            )
        ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    # Foreign key

    # Attributes
    casino_id = models.UUIDField()
    casino_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    external_id = models.CharField(max_length=500)
    last_session = models.DateTimeField()
    state = models.CharField(
        max_length=50, choices=PlayerStateOption.choices, 
        default=PlayerStateOption.OFFLINE
    )
    ban = models.BooleanField(default=False)

    if TYPE_CHECKING:
        total_bets: int
