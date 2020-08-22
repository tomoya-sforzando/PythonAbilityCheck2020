rps_map = {0: "グー", 1: "パー", 2: "チョキ"}

rps_judge_table = ((-1, 1, 0), (1, -1, 2), (0, 2, -1))
"""
Each number mean is winner's hand form.
'0', '1' and '2' are referenced rps_map. '-1' is no winner (equal 'Draw').

e.g.
    `rps_judge_table[0][2]` is return `0`.
    The first selected "グー" and the second selected "チョキ".
    Winner's hand form is "グー", and winner is the first.

    `rps_judge_table[1][2]` is return `2`.
    The first selected "パー" and the second selected "チョキ".
    Winner's hand form is "チョキ", and winner is the second.

    `rps_judge_table[1][1]` is return `-1`.
    The first selected "パー" and the second selected "バー".
    It is no winner and judged "Draw".
"""

players = ("源静香", "ドラえもん", "野比のび太", "骨川スネ夫", "ドラミ")
selectable_hand = {
    "源静香": (0, 1, 2),
    "ドラえもん": (0,),
    "野比のび太": (0, 1, 2),
    "骨川スネ夫": (1, 2),
    "ドラミ": (0, 0, 1, 2)
}
