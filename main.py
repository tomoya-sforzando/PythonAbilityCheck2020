#!/usr/bin/env python3

import argparse
import random
from typing import List, Tuple

import rps_env
from player import Player


def main(players: List[str], trials: int):
    """
    Parameters
    --------
    players: list<str>
        源静香: グー、チョキ、パーをちょうど1/3の確率ずつ出す
        野比のび太: 最初はランダム、勝ったら次も同じ手を出す
        ドラえもん: グーしか出せない
        骨川スネ夫: チョキとパーしか出せない
        ドラミ: グーを50%, チョキとパーを25%の確率で出す
    trials:
        int試行回数（max: 10000）

    Returns
    --------
    要素数=試行回数の配列と勝率配列の要素はタプル
    [("<firstが出した手 {"グー" | "チョキ" | "パー"}>", "<secondが出した手　{"グー" | "チョキ" | "パー"}>",
    "<firstから見た勝敗 {"Win" | "Draw" | "Lose"}>"), ..., ()] <firstの勝率(小数点下2桁)> %

    Raises
    --------
    ValueError引数の文字列や試行回数がおかしい場合

    Examples
    --------
    >>> main("ドラえもん", "野比のび太", 10)
    ドラえもん vs 野比のび太, trials=10
    [("グー", "チョキ", "Win"), ("グー", "グー", "Draw"), ("グー", "パー", "Lose"), ("グー", "パー", "Lose"), ("グー", "パー",
    "Lose"), ("グー", "パー", "Lose"), ("グー", "パー", "Lose"), ("グー", "パー", "Lose"), ("グー", "パー", "Lose"), ("グー",
    "パー", "Lose")] 10.00 % main("源静香", "骨川スネ夫", 10) [("グー", "パー", "Lose"), ("パー", "チョキ", "Lose"), ("パー",
    "チョキ", "Lose"), ("グー", "パー", "Lose"), ("パー", "チョキ", "Lose"), ("グー", "パー", "Lose"), ("チョキ", "チョキ",
    "Draw"), ("グー", "パー", "Lose"), ("チョキ", "パー", "Lose"), ("チョキ", "チョキ", "Lose")] 0.00 %
    """
    # Set player when not selected
    if not players:
        players = []
    if len(players) < 2:
        while len(players) < 2:
            players.append(random.choice(rps_env.players))

    if sum([1 for player_name in players if not isinstance(player_name, str)]) or \
       sum([1 for player_name in players if player_name not in rps_env.players]) or \
       not isinstance(trials, int) or trials < 0 or 10000 < trials:
        raise ValueError()

    player_tuple = tuple(Player(player) for player in players)

    results = rps(player_tuple, trials)

    win_rate = player_tuple[0].get_rate_of_win()
    print(f"{' vs '.join(players)}, {trials=}")
    print(f"{results} {win_rate:.2f} %")


def rps(players: Tuple[Player], trials: int):
    results = []
    for _ in range(trials):
        player_hands = [player.select_hand() for player in players]
        staged_hands = tuple(set(player_hands))
        if len(staged_hands) == 1 or 2 < len(staged_hands):
            for player in players:
                player.record_result("Draw")
        else:
            winner_rps = rps_env.rps_judge_table[staged_hands[0]][staged_hands[1]]
            for player in players:
                if player.get_current_hand() == winner_rps:
                    player.record_result("Win")
                else:
                    player.record_result("Lose")

        hands_ja = [rps_env.rps_map[hand] for hand in player_hands]
        results.append(tuple(hands_ja + [players[0].get_current_result()]))

    return results


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--players", action="append", choices=rps_env.players,
                        help="Set player. Multiple players can be added with the same arguments")
    parser.add_argument("--trials", type=int, default=10, help="Set number of trials. max:10000")
    return parser.parse_args(args)


if __name__ == "__main__":
    import sys

    parser = parse_args(sys.argv[1:])
    main(parser.players, parser.trials)
