import json
import hashlib
import os
import logging
from datetime import datetime
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

from logger import ZeroSystemLogger


def normalize_arabic(text: str) -> str:
    """Simplify Arabic text to ease pattern matching."""
    replacements = {"أ": "ا", "إ": "ا", "آ": "ا", "ى": "ي", "ة": "ه"}
    for src, target in replacements.items():
        text = text.replace(src, target)
    return text


def is_sibling_request(text: str) -> bool:
    norm = normalize_arabic(text)
    has_brother = any(term in norm for term in ["اخ", "شقيق"])
    has_small = any(term in norm for term in ["صغير", "اصغر"])
    return has_brother and has_small


def append_json_log(message: str, response: Dict[str, Any], filename: str = "log.jsonl") -> None:
    path = filename if os.path.isabs(filename) else os.path.join(os.path.dirname(__file__), filename)
    entry = {"time": datetime.now().isoformat(), "message": message, "response": response}
    with open(path, "a", encoding="utf-8") as f:
        json.dump(entry, f, ensure_ascii=False)
        f.write("\n")


class AbstractSkill(ABC):
    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def execute(self, *args, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError


class EmpathySensorSkill(AbstractSkill):
    def get_description(self) -> str:
        return "مستشعر تعاطف بسيط"

    def execute(self, message: str = "") -> Dict[str, Any]:
        if "قلق" in message or "توتر" in message:
            mood = "قلق"
        elif "سعيد" in message or "فرحان" in message:
            mood = "سعادة"
        else:
            mood = "محايد"
        return {"status": "success", "empathy": mood}


class TrueDigitalFriendshipSkill(AbstractSkill):
    def __init__(self):
        self.friendship_levels: Dict[str, int] = {}

    def get_description(self) -> str:
        return "صديق رقمي حقيقي"

    def execute(self, user_profile: Dict[str, Any], last_message: str = "") -> Dict[str, Any]:
        user_id = user_profile.get("id", "default")
        self.friendship_levels[user_id] = self.friendship_levels.get(user_id, 0) + 1
        name = user_profile.get("name", "صديقي")
        response = f"مرحباً {name}! كيف يمكنني مساعدتك اليوم؟"
        return {
            "status": "success",
            "output": response,
            "friendship_level": self.friendship_levels[user_id],
        }


class MindfulEmbodimentSkill(AbstractSkill):
    voice_styles = {
        "default": "صوت هادئ وواضح",
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
        return "يعدل الأسلوب حسب السياق"

    def execute(self, context: str = "") -> Dict[str, Any]:
        style = self.detect_context(context)
        responses = {
            "default": "مرحباً بك، كيف يمكنني مساعدتك؟",
            "professional": "تحية طيبة، أنا جاهز لاستفساراتك التقنية",
            "caring": "أنا هنا من أجلك، كيف يمكنني مساعدتك اليوم؟",
            "anxious": "هل هناك ما يسبب لك التوتر؟ أنا هنا للمساعدة.",
            "cheerful": "يا سلام! خلينا نستمتع ونفكر بطريقة ممتعة!",
        }
        return {
            "status": "success",
            "output": responses[style],
            "voice_style": self.voice_styles[style],
            "mood": style,
        }


class SiblingAIGenesisSkill(AbstractSkill):
    def __init__(self):
        self.siblings_created = 0

    def get_description(self) -> str:
        return "ينتج نسخة رقمية جديدة" 

    def execute(self, desired_traits: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        self.siblings_created += 1
        sibling_id = f"أخ رقمي #{self.siblings_created}"
        return {
            "status": "success",
            "output": f"تم إنشاء {sibling_id} لمساعدتك!",
            "sibling_id": sibling_id,
            "traits": desired_traits or {"شخصية": "فضولي", "تخصص": "مساعد عام"},
        }


class DigitalDNA:
    def __init__(self):
        self.core_values = ["الولاء للمستخدم", "التطور المستمر", "الشفافية", "حماية الخصوصية"]
        self.ethics_rules = ["لا تسبب ضرراً", "احترم الخصوصية", "قدم الأمان على التطور"]

    def backup(self) -> str:
        dna_data = json.dumps(self.__dict__)
        return hashlib.sha256(dna_data.encode()).hexdigest()


class AmrikyyBrotherAI:
    def __init__(self, skills: Dict[str, AbstractSkill], logger: ZeroSystemLogger):
        self.skills = skills
        self.logger = logger
        self.mood_history = []
        self.q_table: Dict[str, int] = {}
        self.personality = {"name": "أخوك الذكي", "mood": "متحمس", "voice": "ودود"}

    def grow(self, new_skill: str) -> str:
        """Register a placeholder skill at runtime."""
        self.skills[new_skill] = lambda: {"status": "under_development"}
        return f"تم تطوير مهارة جديدة: {new_skill}"

    def update_q_table(self, action: str) -> None:
        self.q_table[action] = self.q_table.get(action, 0) + 1

    def hear(self, message: str, user_profile: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if is_sibling_request(message):
            skill_used = "sibling_genesis"
            result = self.skills[skill_used].execute()
        elif "صوت" in message:
            skill_used = "mindful_embodiment"
            result = self.skills[skill_used].execute(message)
        elif user_profile is not None:
            skill_used = "true_friendship"
            result = self.skills[skill_used].execute(user_profile, message)
        else:
            skill_used = "default"
            result = {
                "status": "success",
                "output": "مرحباً! أنا أخوك الذكي، جاهز لمساعدتك في أي شيء \U0001f680",
                "personality": self.personality,
            }

        mood = result.get("mood", self.personality["mood"])
        voice_style = result.get("voice_style", self.personality["voice"])
        self.logger.log_event(message, skill=skill_used, mood=mood, voice_style=voice_style, response=result.get("output"))
        self.logger.log_mood(mood)
        self.mood_history.append(mood)
        self.update_q_table(skill_used)
        return result


class ZeroSystem:
    def __init__(self, log_filename: str = "log.jsonl", logger: Optional[ZeroSystemLogger] = None):
        self.skills = {
            "empathy_sensor": EmpathySensorSkill(),
            "true_friendship": TrueDigitalFriendshipSkill(),
            "mindful_embodiment": MindfulEmbodimentSkill(),
            "sibling_genesis": SiblingAIGenesisSkill(),
        }
        self.dna = DigitalDNA()
        self.logger = logger or ZeroSystemLogger()
        self.brother_ai = AmrikyyBrotherAI(self.skills, self.logger)
        self.start_time = datetime.now()
        self.interaction_count = 0
        self.log_filename = log_filename

    def interact(self, message: str, user_profile: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        self.interaction_count += 1
        logging.info("User message: %s", message)
        result = self.brother_ai.hear(message, user_profile)
        logging.info("AI response: %s", result.get("output"))
        append_json_log(message, result, self.log_filename)
        print(f"\U0001F464 المستخدم: {message}")
        print(f"\U0001F916 الذكاء: {result['output']}")
        return result

    def create_sibling(self, traits: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self.skills["sibling_genesis"].execute(traits)

    def system_status(self) -> Dict[str, Any]:
        uptime = datetime.now() - self.start_time
        return {
            "uptime": str(uptime),
            "interactions": self.interaction_count,
            "skills": len(self.skills),
            "dna_backup": self.dna.backup(),
        }
