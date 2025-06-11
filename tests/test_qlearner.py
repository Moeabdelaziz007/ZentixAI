from zero_system.learning.qlearn import QLearner


def test_qlearner_updates_and_best_action(tmp_path):
    db_file = tmp_path / "q.json"
    q = QLearner(str(db_file), learning_rate=1.0, discount=0.0)
    q.update("s1", "a1", reward=1, next_state="s2")
    assert q.get_best_action("s1") == "a1"

    q.update("s1", "a2", reward=2, next_state="s2")
    assert q.get_best_action("s1") == "a2"

    # values persist
    q2 = QLearner(str(db_file), learning_rate=1.0, discount=0.0)
    assert q2.get_best_action("s1") == "a2"
