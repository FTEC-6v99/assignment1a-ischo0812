from app.src.Player import Player
from app.src.Stats import Stats


class statsheet():
    def __init__(self, player: Player, stats: Stats):
        self.player = player
        self.stats = stats
