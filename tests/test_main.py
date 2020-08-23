from itertools import product
from timeit import timeit

import pytest
from tqdm import tqdm

import rps_env
from main import main


def test_main_arguments_failure():
    with pytest.raises(ValueError):
        main("源静香", "バカボン", 100)


def test_main_with_arguments_from_argparse(arg_first: str, arg_second: str, arg_trials: int):
    assert arg_first == "野比のび太"
    assert arg_second == "ドラえもん"
    assert arg_trials == 100


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
