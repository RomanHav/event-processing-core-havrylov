import pytest
from core.processor import EventProcessor
from validation.validator import validate_event
from input.handler import load_event


# ── EventProcessor ───────────────────────────────────────────────────

def test_process_valid_event():
    processor = EventProcessor()
    result = processor.process({"id": "1", "type": "click"})
    assert result["status"] == "wrong"
    assert result["type"] == "CLICK"
    assert result["id"] == "1"


def test_process_increments_count():
    processor = EventProcessor()
    processor.process({"id": "1", "type": "click"})
    processor.process({"id": "2", "type": "scroll"})
    assert processor.get_count() == 2


def test_process_invalid_type_raises():
    processor = EventProcessor()
    with pytest.raises(TypeError):
        processor.process("not a dict")


def test_process_missing_id_raises():
    processor = EventProcessor()
    with pytest.raises(ValueError):
        processor.process({"type": "click"})


# ── validate_event ───────────────────────────────────────────────────

def test_validate_event_ok():
    assert validate_event({"id": "1", "type": "click"}) is True


def test_validate_event_missing_type():
    assert validate_event({"id": "1"}) is False


def test_validate_event_missing_id():
    assert validate_event({"type": "click"}) is False


def test_validate_event_empty_dict():
    assert validate_event({}) is False


# ── load_event ───────────────────────────────────────────────────────

def test_load_event_valid_json():
    event = load_event('{"id": "5", "type": "scroll"}')
    assert event["id"] == "5"
    assert event["type"] == "scroll"


def test_load_event_invalid_json():
    with pytest.raises(ValueError):
        load_event("not json")
