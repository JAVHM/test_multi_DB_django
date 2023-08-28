import uuid

from django.db import models

from crash_game.enums import RoundStateOption


class Round(models.Model):
    class Meta:
        db_table = "igaming_round"
        constraints = [
            models.UniqueConstraint(
                fields=["position"],
                name="unique_round",
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
    position = models.PositiveBigIntegerField()
    multiplier = models.PositiveBigIntegerField()
    multiplier_hash = models.CharField(max_length=300)
    state = models.CharField(max_length=32, choices=RoundStateOption.choices)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True)
    real_multiplier = models.DecimalField(decimal_places=20, max_digits=100)
