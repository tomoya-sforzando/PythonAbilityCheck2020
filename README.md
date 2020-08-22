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

`$ docker exec pac2020-python python main.py`

or you can set arguments.  
e.g. `$ docker exec pac2020-python python main.py --first ドラえもん --second 野比のび太 --trials 10`

more information for arguments are

```shell
$ docker exec pac2020-python python main.py -h
usage: main.py [-h] [--first {源静香,ドラえもん,野比のび太,骨川スネ夫,ドラミ}]
               [--second {源静香,ドラえもん,野比のび太,骨川スネ夫,ドラミ}] [--trials TRIALS]

optional arguments:
  -h, --help            show this help message and exit
  --first {源静香,ドラえもん,野比のび太,骨川スネ夫,ドラミ}
                        Select the first player
  --second {源静香,ドラえもん,野比のび太,骨川スネ夫,ドラミ}
                        Select the second player
  --trials TRIALS       Set number of trials. max:10000
```

### 3. Test

`$ docker exec pac2020-python pytest . --capture=no`

### 4. Clear docker container and image

`$ docker stop pac2020-python && docker rmi pac2020:latest`

## References

- [Rock Paper Scissors in Python - A Complete Step-By-Step Guide - AskPython](https://www.askpython.com/python/examples/rock-paper-scissors-in-python)
- [argparse --- コマンドラインオプション、引数、サブコマンドのパーサー — Python 3.8.5 ドキュメント](https://docs.python.org/ja/3/library/argparse.html)

## Miscellaneous

None.
