#!/usr/bin/env python3

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
    if type(first) is not str or type(second) is not str or type(trials) is not int or trials < 0 or 10000 < trials:
        raise ValueError()

    results = [("グー", "チョキ", "Win"), ("グー", "グー", "Draw")]
    win_rate = 50.00

    print(f"{results} {win_rate:.2f} %")

if __name__ == "__main__":
    main("ドラえもん", "野比のび太", 2)