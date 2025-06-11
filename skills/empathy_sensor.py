from .base import AbstractSkill


class EmpathySensorSkill(AbstractSkill):
    """Simple empathy sensor based on keyword detection."""

    def get_description(self):
        return "مستشعر تعاطف بسيط يقرأ المشاعر من الكلمات"

    def execute(self, message: str = ""):
        if "قلق" in message or "توتر" in message:
            return {"status": "success", "empathy": "قلق"}
        if "سعيد" in message or "فرحان" in message:
            return {"status": "success", "empathy": "سعادة"}
        return {"status": "success", "empathy": "محايد"}
