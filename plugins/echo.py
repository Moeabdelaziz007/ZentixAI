from zero_system import AbstractSkill


class EchoSkill(AbstractSkill):
    """Simple plugin skill that echoes the provided message."""

    def get_description(self):
        return "Echoes back whatever the user says"

    def execute(self, message: str = "", **kwargs):
        return {"status": "success", "output": message}


def register(skills: dict) -> None:
    skills["echo"] = EchoSkill()
