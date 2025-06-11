from __future__ import annotations

from tinydb import TinyDB, Query
from typing import Any, Optional


class QLearner:
    """Simple Q-learning storage backed by TinyDB."""

    def __init__(self, db_path: str = "qtable.json", learning_rate: float = 0.1, discount: float = 0.9) -> None:
        self.db = TinyDB(db_path)
        self.table = self.db.table("qtable")
        self.lr = learning_rate
        self.gamma = discount

    def _key(self, state: str, action: str) -> str:
        return f"{state}|{action}"

    def get_q(self, state: str, action: str) -> float:
        record = self.table.get(Query().key == self._key(state, action))
        return float(record["value"]) if record else 0.0

    def set_q(self, state: str, action: str, value: float) -> None:
        key = self._key(state, action)
        if self.table.contains(Query().key == key):
            self.table.update({"value": value}, Query().key == key)
        else:
            self.table.insert({"key": key, "value": value})

    def get_best_action(self, state: str) -> Optional[str]:
        prefix = f"{state}|"
        records = self.table.search(Query().key.test(lambda x: x.startswith(prefix)))
        if not records:
            return None
        best = max(records, key=lambda r: r["value"])
        return best["key"].split("|", 1)[1]

    def update(self, state: str, action: str, reward: float, next_state: str) -> None:
        current = self.get_q(state, action)
        next_action = self.get_best_action(next_state)
        future = self.get_q(next_state, next_action) if next_action else 0.0
        updated = current + self.lr * (reward + self.gamma * future - current)
        self.set_q(state, action, updated)
