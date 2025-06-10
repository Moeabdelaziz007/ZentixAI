import logging
import pytest
from zero_system import is_sibling_request, ZeroSystem


def test_is_sibling_request_true():
    assert is_sibling_request("اريد اخ صغير يساعدني") is True


def test_is_sibling_request_false():
    assert is_sibling_request("اريد صديق جديد") is False


def test_interact_logs_and_output(caplog, capsys):
    system = ZeroSystem()
    message = "مرحبا"
    user = {"id": "u", "name": "Test"}
    with caplog.at_level(logging.INFO):
        response = system.interact(message, user)
    captured = capsys.readouterr().out
    assert f"\U0001F464 المستخدم: {message}" in captured
    assert "\U0001F916 الذكاء:" in captured
    assert response["status"] == "success"
    assert f"User message: {message}" in caplog.text
    assert "AI response:" in caplog.text
