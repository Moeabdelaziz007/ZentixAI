"""Simple Q-learning agent with SQLite persistence."""
import sqlite3
from typing import Iterable


class QLearningAgent:
    def __init__(self, db_path: str = "qtable.db", alpha: float = 0.1, gamma: float = 0.9):
        self.conn = sqlite3.connect(db_path)
        self.alpha = alpha
        self.gamma = gamma
        self._init_db()

    def _init_db(self) -> None:
        cur = self.conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS qtable (state TEXT, action TEXT, value REAL, PRIMARY KEY(state, action))"
        )
        self.conn.commit()

    def get(self, state: str, action: str) -> float:
        cur = self.conn.execute("SELECT value FROM qtable WHERE state=? AND action=?", (state, action))
        row = cur.fetchone()
        return row[0] if row else 0.0

    def set(self, state: str, action: str, value: float) -> None:
        self.conn.execute(
            "REPLACE INTO qtable (state, action, value) VALUES (?, ?, ?)",
            (state, action, value),
        )
        self.conn.commit()

    def update(self, state: str, action: str, reward: float, next_state: str, actions: Iterable[str]):
        q_current = self.get(state, action)
        max_next = max((self.get(next_state, a) for a in actions), default=0.0)
        new_value = q_current + self.alpha * (reward + self.gamma * max_next - q_current)
        self.set(state, action, new_value)
        return new_value

    def close(self) -> None:
        self.conn.close()
