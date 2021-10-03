from player import Player
from stats import Stats


class StatSheet():
    def __init__(self, player: Player, stats: Stats):
        self.player = player
        self.stats = stats
