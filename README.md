# Python Ability Check 2020 - KASHIMADA Tomoya

![PAC2020-Python](https://github.com/tomoya-sforzando/PythonAbilityCheck2020/workflows/PAC2020-Python/badge.svg)
[![codecov](https://codecov.io/gh/tomoya-sforzando/PythonAbilityCheck2020/branch/master/graph/badge.svg)](https://codecov.io/gh/tomoya-sforzando/PythonAbilityCheck2020)

## Requirements

- Python 3.8.5
- Docker

## How to Run

### 1. Setup docker container

1. Boot 'Docker Desktop'
1. `$ docker build --pull --rm -f Dockerfile -t pac2020:latest .`
1. `$ docker run -it --rm --name pac2020-python -v "$PWD":/usr/src/app -w /usr/src/app -d pac2020:latest /bin/bash`

### 2. Run

Play games with random 2 Players.
`$ docker exec pac2020-python python main.py`

or you can set arguments.  
e.g. `$ docker exec pac2020-python python main.py --players 源静香 --players 野比のび太 --players ドラえもん --trials 10`

more information for arguments are

```shell
$ docker exec pac2020-python python main.py -h
usage: main.py [-h] [--players {源静香,ドラえもん,野比のび太,骨川スネ夫,ドラミ}] [--trials TRIALS]

optional arguments:
  -h, --help            show this help message and exit
  --players {源静香,ドラえもん,野比のび太,骨川スネ夫,ドラミ}
                        Set player. Multiple players can be added with the
                        same arguments
  --trials TRIALS       Set number of trials. max:10000
```

### 3. Test

`$ docker exec pac2020-python python -m pytest . --capture=no --verbose`

### 4. Clear docker container and image

`$ docker stop pac2020-python && docker rmi pac2020:latest`

## References

- [Rock Paper Scissors in Python - A Complete Step-By-Step Guide - AskPython](https://www.askpython.com/python/examples/rock-paper-scissors-in-python)
- [argparse --- コマンドラインオプション、引数、サブコマンドのパーサー — Python 3.8.5 ドキュメント](https://docs.python.org/ja/3/library/argparse.html)
- [unit testing - How do you write tests for the argparse portion of a python module? - Stack Overflow](https://stackoverflow.com/questions/18160078/how-do-you-write-tests-for-the-argparse-portion-of-a-python-module)

## Miscellaneous

None.
