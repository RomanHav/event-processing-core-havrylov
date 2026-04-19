class EventProcessor:
    def __init__(self):
        self.processed = []

    def process(self, event: dict) -> dict:
        if not isinstance(event, dict):
            raise TypeError("Event must be a dict")
        result = {
            "id": event.get("id"),
            "type": event.get("type", "unknown").upper(),
            "status": "processed",
        }
        self.processed.append(result)
        return result

    def get_count(self) -> int:
        return len(self.processed)