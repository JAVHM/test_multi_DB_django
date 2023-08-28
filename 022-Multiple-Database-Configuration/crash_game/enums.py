from django.db import models


class RoundStateOption(models.TextChoices):
    STARTING = "STARTING", "starting"
    LOCKING = "LOCKING", "locking"
    PLAYING = "PLAYING", "playing"
    ENDING = "ENDING", "ending"


class PlayerStateOption(models.TextChoices):
    OFFLINE = "OFFLINE", "offline"
    ONLINE = "ONLINE", "online"


class DisjoinReasonOption(models.TextChoices):
    CRASH = "CRASH", "crash"
    CASH_OUT = "CASH_OUT", "cash_out"
    LEAVE = "LEAVE", "leave"
    NOT_FINISHED = "NOT_FINISH", "not_finish"
