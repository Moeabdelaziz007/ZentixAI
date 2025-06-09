import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from zero_system import ZeroSystem, is_sibling_request


def test_is_sibling_request_detects_true():
    assert is_sibling_request("اريد اخ صغير يساعدني")


def test_is_sibling_request_detects_false():
    assert not is_sibling_request("مرحبا كيف الحال")


def test_zero_system_status_contains_fields():
    system = ZeroSystem()
    status = system.system_status()
    assert "uptime" in status
    assert "interactions" in status
    assert "skills" in status
    assert "dna_backup" in status


def test_create_sibling_increments_count():
    system = ZeroSystem()
    first = system.create_sibling()
    second = system.create_sibling()
    assert first["sibling_id"] != second["sibling_id"]
