import pytest
from tqdm import tqdm

from itertools import product
from random import randint
from timeit import timeit

from main import main, rps
from player import Player
import rps_env


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


@pytest.mark.skip()
def measure_time(stmt: str, trials: int = 100) -> float:
    t = timeit(stmt, globals=globals(), number=trials)
    print(f"{stmt} took {t} seconds for {trials} attempts.")
    return t


def test_main():
    assert dir(main)
    matches = list(product(rps_env.player, repeat=2))
    for first, second in tqdm(matches):
        assert measure_time(f"main('{first}', '{second}', 1000)", 16) < 1.0
