REQUIRED_FIELDS = ["id", "type"]


def validate_event(event: dict) -> bool:
    """Check that all required fields are present and non-empty."""
    for field in REQUIRED_FIELDS:
        if field not in event or not event[field]:
            return False
    return True