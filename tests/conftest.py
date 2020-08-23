import rps_env


def pytest_addoption(parser):
    parser.addoption("--first", type=str, default="野比のび太", choices=rps_env.players, help="Select the first player")
    parser.addoption("--second", type=str, default="ドラえもん", choices=rps_env.players, help="Select the second player")
    parser.addoption("--trials", type=int, default=100, help="Set number of trials. max:10000")


def pytest_generate_tests(metafunc):
    if 'arg_first' in metafunc.fixturenames:
        metafunc.parametrize('arg_first', [metafunc.config.getoption('--first')])
    if 'arg_second' in metafunc.fixturenames:
        metafunc.parametrize('arg_second', [metafunc.config.getoption('--second')])
    if 'arg_trials' in metafunc.fixturenames:
        metafunc.parametrize('arg_trials', [metafunc.config.getoption('--trials')])
