from itertools import product
from math import isclose
from timeit import timeit

import pytest
from tqdm import tqdm

import rps_env
from main import main, rps
from player import Player


def test_rate_of_shizuka_selected(trials: int = 10000, relative_tolerance: float = 0.1):
    shizuka = Player("源静香")
    doraemon = Player("ドラえもん")
    nobita = Player("野比のび太")
    suneo = Player("骨川スネ夫")
    dorami = Player("ドラミ")
    players = [shizuka, doraemon, nobita, suneo, dorami]

    for player in tqdm(players):
        rps(shizuka, player, round(trials / len(players)))

    print(shizuka.get_rate_of_selected_hand(0))

    assert isclose(100 / 3, shizuka.get_rate_of_selected_hand(0), rel_tol=relative_tolerance)
    assert isclose(100 / 3, shizuka.get_rate_of_selected_hand(1), rel_tol=relative_tolerance)
    assert isclose(100 / 3, shizuka.get_rate_of_selected_hand(2), rel_tol=relative_tolerance)


@pytest.mark.skip()
def measure_time(stmt: str, trials: int = 100) -> float:
    t = timeit(stmt, globals=globals(), number=trials)
    print(f"{stmt} took {t} seconds for {trials} attempts.")
    return t


def test_main():
    assert dir(main)
    matches = list(product(rps_env.players, repeat=2))
    for first, second in tqdm(matches):
        assert measure_time(f"main('{first}', '{second}', 1000)", 16) < 1.0
