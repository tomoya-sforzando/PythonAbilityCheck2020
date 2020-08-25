from math import isclose
import random

import pytest
from tqdm import tqdm

import rps_env
from player import Player


def test_make_instance():
    shizuka = Player("源静香")
    assert shizuka.name == "源静香"


def test_get_current_hand():
    shizuka = Player("源静香")
    current_hand = ""
    for _ in range(10):
        current_hand = shizuka.select_hand()
    assert shizuka.get_current_hand() == current_hand


def test_get_current_result():
    shizuka = Player("源静香")
    current_result = ""
    for _ in range(10):
        current_result = random.choice(["Win", "Lose", "Draw"])
        shizuka.record_result(current_result)
    assert shizuka.get_current_result() == current_result


@pytest.mark.skip()
def get_rate_of_rps(player: Player, trials: int):
    for _ in tqdm(range(trials)):
        player.select_hand()
    rate_of_rock_selected = player.get_rate_of_selected_hand(0)
    rate_of_paper_selected = player.get_rate_of_selected_hand(1)
    rate_of_scissors_selected = player.get_rate_of_selected_hand(2)
    print(f"\n{player.name=}")
    print(f"{rate_of_rock_selected=}")
    print(f"{rate_of_paper_selected=}")
    print(f"{rate_of_scissors_selected=}")
    return rate_of_rock_selected, rate_of_paper_selected, rate_of_scissors_selected


@pytest.mark.parametrize('player_name', rps_env.players)
def test_rate_of_selected_hand(player_name: str, trials: int = 10000, relative_tolerance: float = 0.05):
    player = Player(player_name)
    rate_of_rps = get_rate_of_rps(player, trials)

    if player.name in ("源静香", "野比のび太"):
        assert isclose(100 / 3, rate_of_rps[0], rel_tol=relative_tolerance)
        assert isclose(100 / 3, rate_of_rps[1], rel_tol=relative_tolerance)
        assert isclose(100 / 3, rate_of_rps[2], rel_tol=relative_tolerance)
    if player.name == "ドラえもん":
        assert isclose(100, rate_of_rps[0], rel_tol=relative_tolerance)
    if player.name == "骨川スネ夫":
        assert isclose(0, rate_of_rps[0], rel_tol=relative_tolerance)
        assert isclose(50, rate_of_rps[1], rel_tol=relative_tolerance)
        assert isclose(50, rate_of_rps[2], rel_tol=relative_tolerance)
    if player.name == "ドラミ":
        assert isclose(50, rate_of_rps[0], rel_tol=relative_tolerance)
        assert isclose(25, rate_of_rps[1], rel_tol=relative_tolerance)
        assert isclose(25, rate_of_rps[2], rel_tol=relative_tolerance)
