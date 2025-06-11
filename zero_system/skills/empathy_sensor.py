from .base import AbstractSkill


class EmpathySensorSkill(AbstractSkill):
    """Detect simple emotions from Arabic keywords."""

    def get_description(self) -> str:
        return "مستشعر تعاطف بسيط يقرأ المشاعر من الكلمات"

    def execute(self, message: str = ""):
        if "قلق" in message or "توتر" in message:
            mood = "قلق"
        elif "سعيد" in message or "فرحان" in message:
            mood = "سعادة"
        else:
            mood = "محايد"
        return {"status": "success", "empathy": mood}
