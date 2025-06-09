import json
from datetime import datetime


class ZeroSystemLogger:
    """Simple logger that records interactions to a file."""

    def __init__(self, log_file: str = "zero_system.log") -> None:
        self.log_file = log_file

    def log_interaction(self, message: str, response: dict) -> None:
        """Append a log entry containing the user message and system response."""
        entry = {
            "time": datetime.now().isoformat(),
            "message": message,
            "response": response.get("output"),
        }
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
