import random

import rps_env


class Player:
    def __init__(self, name: str):
        self._name = name
        self.selectable_hand = rps_env.selectable_hand.get(name)
        self.selects = []
        self.results = []

    @property
    def name(self):
        return self._name

    def select_hand(self) -> int:
        # Special rule
        if self._name == "野比のび太" and len(self.results):
            if self.results[-1] == "Win":
                self.selects.append(self.selects[-1])
                return self.selects[-1]

        selected = random.choice(self.selectable_hand)
        self.selects.append(selected)
        return selected

    def get_current_hand(self) -> int:
        return self.selects[-1]

    def get_current_result(self) -> int:
        return self.results[-1]

    def record_result(self, result: str):
        self.results.append(result)

    def get_rate_of_selected_hand(self, rps: int) -> float:
        return self.selects.count(rps) / len(self.selects) * 100

    def get_rate_of_win(self) -> float:
        return self.results.count('Win') / len(self.results) * 100
