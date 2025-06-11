import io
import contextlib
import logging
import sss.zero_system as zs


def test_interact_logs_and_output(caplog):
    system = zs.ZeroSystem()
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
    assert "AI response" in log_text
