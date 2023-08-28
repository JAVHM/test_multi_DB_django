import uuid

from django.db import models


class Bound(models.Model):
    class Meta:
        db_table = "igaming_bound"
        constraints = [
            models.UniqueConstraint(
                fields=["version", "casino_id"],
                name="unique_bound",
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
    currency_code = models.CharField(max_length=15)
    money_precision = models.PositiveBigIntegerField()
    min_bet = models.DecimalField(decimal_places=20, max_digits=100)
    max_bet = models.PositiveBigIntegerField()
    max_profit = models.PositiveBigIntegerField()
    version = models.PositiveBigIntegerField()
