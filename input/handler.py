import json

def load_event(raw: str) -> dict:
    """Parse raw JSON string into event dict."""
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e}")