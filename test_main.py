from random import randint
from main import rps
from player import Player


def test_win_rate_of_shizuka():
    shizuka = Player("源静香")
    doraemon = Player("ドラえもん")
    nobita = Player("野比のび太")
    suneo = Player("骨川スネ夫")
    dorami = Player("ドラミ")
    players = [shizuka, doraemon, nobita, suneo, dorami]
    for i in range(10000):
        rps(shizuka, players[randint(0, len(players) - 1)], 1)

    assert 23.33 < shizuka.win_rate() and shizuka.win_rate() < 43.33
