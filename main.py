#!/usr/bin/env python3

from player import Player
import rps_env


def main(first: str, second: str, trials: int):
    """
    Parameters
    --------
    first, second: string
        源静香: グー、チョキ、パーをちょうど1/3の確率ずつ出す。
        野比のび太: 最初はランダム、勝ったら次も同じ手を出す。
        ドラえもん: グーしか出せない。
        骨川スネ夫: チョキとパーしか出せない。
    trials: int
        試行回数（max: 10000）

    Returns
    --------
    要素数=試行回数の配列と勝率
    配列の要素はタプル
        [("<firstが出した手 {"グー" | "チョキ" | "パー"}>", "<secondが出した手 {"グー" | "チョキ" | "パー"}>", "<firstから見た勝敗 {"Win" | "Draw" | "Lose"}>"), ..., ()] <firstの勝率(小数点下2桁)> %

    Raises
    --------
    ValueError
        引数の文字列や試行回数がおかしい場合

    Examples
    --------
    >>> main("ドラえもん", "野比のび太", 10)
    [("グー", "チョキ", "Win"), ("グー", "グー", "Draw"), ("グー", "パー", "Lose"), ("グー", "パー", "Lose"), ("グー", "パー", "Lose"), ("グー", "パー", "Lose"), ("グー", "パー", "Lose"), ("グー", "パー", "Lose"), ("グー", "パー", "Lose"), ("グー", "パー", "Lose")] 10.00 %
    >>> main("源静香", "骨川スネ夫", 10)
    [("グー", "パー", "Lose"), ("パー", "チョキ", "Lose"), ("パー", "チョキ", "Lose"), ("グー", "パー", "Lose"), ("パー", "チョキ", "Lose"), ("グー", "パー", "Lose"), ("チョキ", "チョキ", "Draw"), ("グー", "パー", "Lose"), ("チョキ", "パー", "Lose"), ("チョキ", "チョキ", "Lose")] 0.00 %
    """
    if not isinstance(
            first,
            str) or first not in rps_env.player or not isinstance(
            second,
            str) or second not in rps_env.player or not isinstance(
                trials,
            int) or trials < 0 or 10000 < trials:
        raise ValueError()

    player_1st = Player(first)
    player_2nd = Player(second)

    results = rps(player_1st, player_2nd, trials)

    win_rate = player_1st.win_rate()
    print(f"{results} {win_rate:.2f} %")


def rps(player_1st: Player, player_2nd: Player, trials: int):
    results = []
    for i in range(trials):
        player_1st_rps = player_1st.select_rps()
        player_2nd_rps = player_2nd.select_rps()
        winner_rps = rps_env.rps_table[player_1st_rps][player_2nd_rps]
        if winner_rps == player_1st_rps:
            player_1st.record_result("Win")
            player_2nd.record_result("Lose")
        elif winner_rps == player_2nd_rps:
            player_1st.record_result("Lose")
            player_2nd.record_result("Win")
        else:
            player_1st.record_result("Draw")
            player_2nd.record_result("Draw")
        results.append((rps_env.game_map[player_1st_rps],
                        rps_env.game_map[player_2nd_rps],
                        player_1st.results[-1]))
    return results


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--first", type=str, default="源静香", choices=[
                        "源静香", "ドラえもん", "野比のび太", "骨川スネ夫", "ドラミ"])
    parser.add_argument("--second", type=str, default="ドラミ", choices=[
                        "源静香", "ドラえもん", "野比のび太", "骨川スネ夫", "ドラミ"])
    parser.add_argument("--trials", type=int, default=1000)
    args = parser.parse_args()

    main(args.first, args.second, args.trials)
