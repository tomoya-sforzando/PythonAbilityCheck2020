from itertools import product
from timeit import timeit

import pytest
from tqdm import tqdm

import rps_env
from player import Player
from main import main, rps, parse_args


def test_main_arguments_failure():
    with pytest.raises(ValueError):
        main(["源静香", "バカボン"], 100)


def test_select_no_players(capfd):
    players = []
    main(players, 100)
    captured = capfd.readouterr()
    assert " vs " in captured.out
    assert "trials=100" in captured.out


def test_select_two_players(capfd):
    players = ["源静香", "野比のび太"]
    main(players, 100)
    captured = capfd.readouterr()
    assert "源静香" in captured.out
    assert "野比のび太" in captured.out


def test_select_five_players(capfd):
    players = ["源静香", "ドラえもん", "野比のび太", "骨川スネ夫", "ドラミ"]
    main(players, 100)
    captured = capfd.readouterr()
    assert "源静香" in captured.out
    assert "ドラえもん" in captured.out
    assert "野比のび太" in captured.out
    assert "骨川スネ夫" in captured.out
    assert "ドラミ" in captured.out


def test_number_of_trials():
    players = ["源静香", "野比のび太"]
    results = rps(tuple(Player(player) for player in players), 100)
    assert len(results) == 100


def test_argument_parser():
    parser = parse_args(["--players", "野比のび太", "--players", "ドラえもん", "--trials", "100"])
    assert parser.players == ["野比のび太", "ドラえもん"]
    assert parser.trials == 100


@pytest.mark.skip()
def measure_time(stmt: str, trials: int = 100) -> float:
    t = timeit(stmt, globals=globals(), number=trials)
    print(f"{stmt} took {t} seconds for {trials} attempts.")
    return t


def test_main():
    assert dir(main)
    matches = list(product(rps_env.players, repeat=2))
    for first, second in tqdm(matches):
        assert measure_time(f"main({[first, second]}, 1000)", 16) < 1.0
