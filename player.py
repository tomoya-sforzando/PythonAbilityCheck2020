import random
import rps_env


class Player:
    def __init__(self, name: str):
        self._name = name
        self.selectable_rps = rps_env.players_rps.get(name)
        self.selects = []
        self.results = []

    @property
    def name(self):
        return self._name

    def select_rps(self) -> int:
        # Special rule
        if self._name == "野比のび太" and len(self.results):
            if self.results[-1] == "Win":
                self.selects.append(self.selects[-1])
                return self.selects[-1]

        selected = random.choice(self.selectable_rps)
        self.selects.append(selected)
        return selected

    def record_result(self, result: str):
        self.results.append(result)

    def selected_rate(self, rps: int) -> float:
        return self.selects.count(rps) / len(self.selects) * 100

    def win_rate(self) -> float:
        return self.results.count('Win') / len(self.results) * 100
