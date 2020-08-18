import random
import rps_env


class Player:
    def __init__(self, name: str):
        self.name = name
        self.rps = rps_env.players_rps.get(name)
        self.selects = []
        self.results = []

    def select_rps(self) -> int:
        # Special rule
        if self.name == "野比のび太" and len(self.results):
            if self.results[-1] == "Win":
                self.selects.append(self.selects[-1])
                return self.selects[-1]

        selected = random.choice(self.rps)
        self.selects.append(selected)
        return selected

    def record_result(self, result: str):
        self.results.append(result)

    def calculate_win_rate(self) -> float:
        return self.results.count('Win') / len(self.results) * 100
