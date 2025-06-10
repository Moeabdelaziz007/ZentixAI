import logging
import io
import contextlib

import pytest

from sss.zero_system import is_sibling_request, ZeroSystem


def test_is_sibling_request_true():
    assert is_sibling_request("اريد اخ صغير يساعدني")


def test_is_sibling_request_false():
    assert not is_sibling_request("اريد صديق جديد")


def test_interact_logs_and_output(caplog):
    system = ZeroSystem()
    message = "مرحبا"
    user = {"id": "u", "name": "Test"}
    buf = io.StringIO()
    with caplog.at_level(logging.INFO), contextlib.redirect_stdout(buf):
        response = system.interact(message, user)
    captured = buf.getvalue()
    assert f"\U0001F464 المستخدم: {message}" in captured
    assert "\U0001F916 الذكاء:" in captured
    assert response["status"] == "success"
    log_text = "\n".join(caplog.messages)
    assert f"User message: {message}" in log_text
    assert any("AI response:" in m for m in caplog.messages)
