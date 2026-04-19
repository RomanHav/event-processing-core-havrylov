import logging

logger = logging.getLogger(__name__)

class EventProcessor:
    def __init__(self, log_level=logging.INFO):  # ← змінили
        self.processed = []
        logging.basicConfig(                      # ← додали
            level=log_level,
            format="%(asctime)s [%(levelname)s] %(message)s"
        )

    def process(self, event: dict) -> dict:
        if not isinstance(event, dict):
            raise TypeError("Event must be a dict")

        if event.get("id") is None:
            raise ValueError("Event must have an 'id' field")

        logger.debug(f"Processing event: {event}")  # ← додали
        result = {
            "id": event.get("id"),
            "type": event.get("type", "unknown").upper(),
            "status": "completed",
        }
        self.processed.append(result)
        logger.info(f"Event processed: {result}")
        return result

    def get_count(self) -> int:
        logger.debug(f"Total processed: {len(self.processed)}")  # ← додали
        return len(self.processed)