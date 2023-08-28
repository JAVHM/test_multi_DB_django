import uuid

from django.db import models

from crash_game.enums import DisjoinReasonOption
from crash_game.modelos.bound import Bound
from crash_game.modelos.player import Player
from crash_game.modelos.round import Round


class Bet(models.Model):
    class Meta:
        db_table = "igaming_bet"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    # Foreign key
    bound = models.ForeignKey(Bound, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    round = models.ForeignKey(Round, on_delete=models.PROTECT)

    # Attributes
    currency_code = models.CharField(max_length=15)
    budget = models.PositiveBigIntegerField()
    amount = models.PositiveBigIntegerField()
    profit = models.PositiveBigIntegerField(null=True)
    cash_out_multiplier = models.PositiveBigIntegerField(null=True)
    join_time = models.DateTimeField()
    disjoin_time = models.DateTimeField(null=True, default=None)
    disjoin_reason = models.CharField(
        max_length=32, choices=DisjoinReasonOption.choices, 
        default=DisjoinReasonOption.NOT_FINISHED
    )
    real_cash_out_multiplier = models.DecimalField(decimal_places=20, max_digits=100, null=True)
    casino_budget = models.DecimalField(decimal_places=20, max_digits=100)
    casino_amount = models.DecimalField(decimal_places=20, max_digits=100)
    casino_profit = models.DecimalField(decimal_places=20, max_digits=100, null=True)
    reported_budget = models.DecimalField(decimal_places=20, max_digits=100)
    reported_amount = models.DecimalField(decimal_places=20, max_digits=100)
    reported_profit = models.DecimalField(decimal_places=20, max_digits=100, null=True)
