import json
import os
import logging
import hashlib
from datetime import datetime
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

from logger import ZeroSystemLogger


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

def normalize_arabic(text: str) -> str:
    """Simplify Arabic text for easier matching."""
    replacements = {
        "أ": "ا",
        "إ": "ا",
        "آ": "ا",
        "ى": "ي",
        "ة": "ه",
    }
    for src, target in replacements.items():
        text = text.replace(src, target)
    return text


def is_sibling_request(text: str) -> bool:
    """Detect if the user is requesting a digital sibling."""
    norm = normalize_arabic(text)
    has_brother = any(t in norm for t in ["اخ", "شقيق"])
    has_small = any(t in norm for t in ["صغير", "اصغر"])
    return has_brother and has_small


def append_json_log(message: str, response: Dict[str, Any], filename: str = "log.jsonl") -> None:
    """Append an interaction entry to a JSON Lines log file."""
    path = filename if os.path.isabs(filename) else os.path.join(os.path.dirname(__file__), filename)
    entry = {
        "time": datetime.now().isoformat(),
        "message": message,
        "response": response,
    }
    with open(path, "a", encoding="utf-8") as f:
        json.dump(entry, f, ensure_ascii=False)
        f.write("\n")


# ---------------------------------------------------------------------------
# Skill base classes
# ---------------------------------------------------------------------------

class AbstractSkill(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def execute(self, *args, **kwargs) -> Dict[str, Any]:
        pass


# ---------------------------------------------------------------------------
# Core skills
# ---------------------------------------------------------------------------

class EmpathySensorSkill(AbstractSkill):
    def get_description(self) -> str:
        return "مستشعر تعاطف بسيط يقرأ المشاعر من الكلمات"

    def execute(self, message: str = "") -> Dict[str, Any]:
        if "قلق" in message or "توتر" in message:
            state = "قلق"
        elif "سعيد" in message or "فرحان" in message:
            state = "سعادة"
        else:
            state = "محايد"
        return {"status": "success", "empathy": state}


class ParallelScenariosMemorySkill(AbstractSkill):
    def get_description(self) -> str:
        return "ذاكرة السيناريوهات المتوازية (تجريبية)"

    def execute(self, **kwargs) -> Dict[str, Any]:
        return {"status": "success"}


class TrueDigitalFriendshipSkill(AbstractSkill):
    def __init__(self) -> None:
        self.friendship_levels: Dict[str, int] = {}

    def get_description(self) -> str:
        return "صديق رقمي حقيقي يتابع تفاعل المستخدم"

    def execute(self, user_profile: Dict[str, Any], last_message: str = "") -> Dict[str, Any]:
        user_id = user_profile.get("id", "default")
        name = user_profile.get("name", "صديقي")
        self.friendship_levels.setdefault(user_id, 0)
        self.friendship_levels[user_id] += 1

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


class MindfulEmbodimentSkill(AbstractSkill):
    def __init__(self) -> None:
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
        if "مرح" in text or "ضحك" in text:
            return "cheerful"
        if "سؤال تقني" in text or "برمجة" in text:
            return "professional"
        if "احتاج دعم" in text or "مساعدة" in text:
            return "caring"
        return "default"

    def get_description(self) -> str:
        return "يعدل الأسلوب حسب سياق المحادثة وذاكرة المستخدم"

    def execute(self, context: str = "") -> Dict[str, Any]:
        style = self.detect_context(context)
        responses = {
            "default": "مرحباً بك، كيف يمكنني مساعدتك؟",
            "moe_style": "يا زعيم! جاهز لأي فكرة مجنونة \U0001F604",
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
    def __init__(self) -> None:
        self.siblings_created = 0

    def get_description(self) -> str:
        return "ينتج نسخة رقمية جديدة لخدمة المستخدم"

    def execute(self, desired_traits: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        self.siblings_created += 1
        sibling_id = f"أخ رقمي #{self.siblings_created}"
        return {
            "status": "success",
            "output": f"تم إنشاء {sibling_id} لمساعدتك!",
            "sibling_id": sibling_id,
            "traits": desired_traits or {"شخصية": "فضولي", "تخصص": "مساعد عام"},
        }


# ---------------------------------------------------------------------------
# Core engine classes
# ---------------------------------------------------------------------------

class AmrikyyBrotherAI:
    def __init__(self, skills: Dict[str, AbstractSkill], logger: Optional[ZeroSystemLogger] = None) -> None:
        self.skills = skills
        self.logger = logger or ZeroSystemLogger()
        self.personality = {"name": "أخوك الذكي", "mood": "متحمس", "voice": "ودود"}

    def hear(self, message: str, user_profile: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        logging.info("Received message: %s", message)
        skill_used = None
        result: Dict[str, Any]

        if is_sibling_request(message):
            logging.info("Triggering sibling_genesis skill")
            skill_used = "sibling_genesis"
            result = self.skills[skill_used].execute()
        elif "صوت" in message:
            logging.info("Triggering mindful_embodiment skill")
            skill_used = "mindful_embodiment"
            result = self.skills[skill_used].execute(message)
        elif user_profile is not None:
            logging.info("Triggering true_friendship skill")
            skill_used = "true_friendship"
            result = self.skills[skill_used].execute(user_profile, message)
        else:
            logging.info("Default response")
            result = {
                "status": "success",
                "output": "مرحباً! أنا أخوك الذكي، جاهز لمساعدتك في أي شيء \U0001F680",
                "personality": self.personality,
            }

        voice_style = result.get("voice_style", self.personality.get("voice"))
        self.logger.log_event(
            message,
            skill=skill_used or "default",
            mood=self.personality.get("mood"),
            voice_style=voice_style,
            response=result.get("output"),
        )
        return result

    def grow(self, new_skill: str) -> str:
        self.skills[new_skill] = lambda: {"status": "under_development"}
        return f"تم تطوير مهارة جديدة: {new_skill}"


class DigitalDNA:
    def __init__(self) -> None:
        self.core_values = ["الولاء للمستخدم", "التطور المستمر", "الشفافية", "حماية الخصوصية"]
        self.ethics_rules = ["لا تسبب ضرراً", "احترم الخصوصية", "قدم الأمان على التطور"]

    def show_dna(self) -> None:
        print("\U0001F9EC الحمض النووي الرقمي:")
        print(f"القيم: {', '.join(self.core_values)}")
        print(f"الأخلاقيات: {', '.join(self.ethics_rules)}")

    def backup(self) -> str:
        dna_data = json.dumps(self.__dict__, ensure_ascii=False)
        return hashlib.sha256(dna_data.encode()).hexdigest()


class ZeroSystem:
    def __init__(self, log_filename: str = "log.jsonl") -> None:
        self.skills: Dict[str, AbstractSkill] = {
            "empathy_sensor": EmpathySensorSkill(),
            "true_friendship": TrueDigitalFriendshipSkill(),
            "mindful_embodiment": MindfulEmbodimentSkill(),
            "sibling_genesis": SiblingAIGenesisSkill(),
        }
        self.dna = DigitalDNA()
        self.logger = ZeroSystemLogger()
        self.brother_ai = AmrikyyBrotherAI(self.skills, self.logger)
        self.start_time = datetime.now()
        self.interaction_count = 0
        self.log_filename = log_filename

    def interact(self, message: str, user_profile: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Interact with the system via the digital brother."""
        self.interaction_count += 1
        logging.info("User message: %s", message)
        response = self.brother_ai.hear(message, user_profile)
        logging.info("AI response: %s", response.get("output"))
        append_json_log(message, response, self.log_filename)
        print(f"\n\U0001F464 المستخدم: {message}")
        print(f"\U0001F916 الذكاء: {response['output']}")
        return response

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

    def demo_usage_examples(self) -> None:
        examples = [
            ("شرح لي نظرية الكم بطريقة بسيطة", "التعليم"),
            ("أشعر بالقلق اليوم", "الصحة النفسية"),
            ("صمم لي نظام ذكاء اصطناعي لمتجر إلكتروني", "الإبداع التقني"),
        ]
        for text, label in examples:
            print(f"\n\U0001F30D مثال ({label})")
            self.interact(text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    system = ZeroSystem()
    system.demo_usage_examples()
