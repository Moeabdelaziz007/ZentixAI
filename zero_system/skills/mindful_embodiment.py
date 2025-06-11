from .base import AbstractSkill


class MindfulEmbodimentSkill(AbstractSkill):
    """Change style based on context."""

    def __init__(self):
        self.voice_styles = {
            "default": "صوت هادئ وواضح",
            "moe_style": "صوت حيوي وساخر",
            "professional": "صوت رسمي وتحليلي",
            "caring": "صوت دافئ ومتعاطف",
            "anxious": "صوت متوتر وسريع",
            "cheerful": "صوت سعيد ومتفائل",
        }

    def detect_context(self, text: str) -> str:
        if "قلق" in text or "توتر" in text:
            return "anxious"
        elif "مرح" in text or "ضحك" in text:
            return "cheerful"
        elif "سؤال تقني" in text:
            return "professional"
        elif "احتاج دعم" in text:
            return "caring"
        else:
            return "default"

    def get_description(self) -> str:
        return "يعدل الأسلوب حسب سياق المحادثة"

    def execute(self, context: str = ""):
        style = self.detect_context(context)
        responses = {
            "default": "مرحباً بك، كيف يمكنني مساعدتك؟",
            "moe_style": "يا زعيم! جاهز لأي فكرة مجنونة \U0001f604",
            "professional": "تحية طيبة، أنا جاهز لاستفساراتك التقنية",
            "caring": "أنا هنا من أجلك، كيف يمكنني مساعدتك اليوم؟",
            "anxious": "هل هناك ما يسبب لك التوتر؟ أنا هنا للمساعدة.",
            "cheerful": "يا سلام! لنستمتع بالتفكير!",
        }
        return {
            "status": "success",
            "output": responses[style],
            "voice_style": self.voice_styles[style],
            "mood": style,
        }
