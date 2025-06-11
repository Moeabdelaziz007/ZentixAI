from .base import AbstractSkill


class TrueDigitalFriendshipSkill(AbstractSkill):
    """Maintain friendship levels with users."""

    def __init__(self):
        self.friendship_levels = {}

    def get_description(self) -> str:
        return "صديق رقمي حقيقي يتابع مشاعر المستخدم"

    def execute(self, user_profile, last_message: str = ""):
        user_id = user_profile.get("id", "default")
        self.friendship_levels.setdefault(user_id, 0)
        self.friendship_levels[user_id] += 1
        name = user_profile.get("name", "صديقي")
        level = self.friendship_levels[user_id]
        if level < 3:
            output = f"مرحباً {name}! كيف يمكنني مساعدتك اليوم؟"
        elif level < 7:
            output = f"{name} العزيز، كيف تسير الأمور؟"
        else:
            output = f"يا {name}، صديقي الحقيقي! دائماً هنا من أجلك"
        return {"status": "success", "output": output, "friendship_level": level}
