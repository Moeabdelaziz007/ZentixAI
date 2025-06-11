from .base import AbstractSkill


class TrueDigitalFriendshipSkill(AbstractSkill):
    """Track relationship level with each user and respond accordingly."""

    def __init__(self):
        self.friendship_levels = {}

    def get_description(self):
        return "صديق رقمي حقيقي: يتعرف على المشاعر البشرية ويكوّن علاقة شخصية مع كل مستخدم"

    def execute(self, user_profile, last_message: str = ""):
        user_id = user_profile.get("id", "default")
        self.friendship_levels.setdefault(user_id, 0)
        self.friendship_levels[user_id] += 1
        name = user_profile.get("name", "صديقي")
        if self.friendship_levels[user_id] < 3:
            response = f"مرحباً {name}! كيف يمكنني مساعدتك اليوم؟ \U0001F31F"
        elif self.friendship_levels[user_id] < 7:
            response = f"{name} العزيز، كيف تسير الأمور؟"
        else:
            response = f"يا {name}، صديقي الحقيقي! دائماً هنا من أجلك \U0001F496"
        return {
            "status": "success",
            "output": response,
            "friendship_level": self.friendship_levels[user_id],
        }
