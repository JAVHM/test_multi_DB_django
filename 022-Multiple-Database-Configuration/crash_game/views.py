from django.views.generic.edit import CreateView
from .models import Crash_Game
from crash_game.modelos.bet import Bet


class Add(CreateView):
    model = Crash_Game
    fields = ('title', 'content', 'app_name')
    template_name = 'add.html'
    success_url = '/crash_game/'


class Add2(CreateView):
    model = Bet
    fields = ('title', 'content', 'app_name', 'test')
    template_name = 'add1.html'
    success_url = '/crash_game/'