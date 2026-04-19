class EventProcessor:
    def __init__(self):
        self.processed = []

    def process(self, event: dict) -> dict:
        if not isinstance(event, dict):
            raise TypeError("Event must be a dict")

        if event.get("id") is None:
            raise ValueError("Event must have an 'id' field")

        result = {
            "id": event.get("id"),
            "type": event.get("type", "unknown").upper(),
            "status": "completed",
        }
        self.processed.append(result)
        return result

    def get_count(self) -> int:
        return len(self.processed)