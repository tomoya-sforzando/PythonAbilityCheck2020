# Python Ability Check 2020 - KASHIMADA Tomoya

## Requirements

- Python 3.8.5
- Docker

## How to Run

### 1. Setup docker container
1. Boot 'Docker Desktop'
1. `$ docker-compose up --detach --build`

### 2. Run
`$ docker-compose run python385 python main.py`

or you can set arguments.  
e.g. `$ docker-compose run python385 python main.py --first ドラえもん --second 野比のび太 --trials 10`

### 3. Test

`$ docker-compose run python385 pytest .`

### 4. Close docker container

`$ docker-compose down --remove-orphans`

## References

- [Rock Paper Scissors in Python \- A Complete Step\-By\-Step Guide \- AskPython](https://www.askpython.com/python/examples/rock-paper-scissors-in-python)
- [argparse \-\-\- コマンドラインオプション、引数、サブコマンドのパーサー — Python 3\.8\.5 ドキュメント](https://docs.python.org/ja/3/library/argparse.html)

## Miscellaneous

None.
