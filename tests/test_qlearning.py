import os
from zero_system.learning.qlearn import QLearningAgent


def test_qlearning_persistence(tmp_path):
    db = tmp_path / "q.db"
    agent = QLearningAgent(str(db))
    agent.update("s1", "a1", 1.0, "s2", ["a1"])
    value = agent.get("s1", "a1")
    agent.close()

    agent2 = QLearningAgent(str(db))
    assert agent2.get("s1", "a1") == value
    agent2.close()
