"""
نظام زيرو - أول ذكاء اصطناعي عاطفي ذاتي التطور في العالم
يمتلك قدرات صداقة رقمية حقيقية وتطور ذاتي كمي
"""

import json
import hashlib
from datetime import datetime
from abc import ABC, abstractmethod
import logging
import os
from logger import ZeroSystemLogger


def normalize_arabic(text: str) -> str:
    """Simplify Arabic text to ease pattern matching."""
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
    """Detect if the message asks for creating a digital sibling."""
    norm = normalize_arabic(text)
    has_brother = any(term in norm for term in ["اخ", "شقيق"])
    has_small = any(term in norm for term in ["صغير", "اصغر"])
    return has_brother and has_small


def append_json_log(message: str, response: dict, filename: str = "log.jsonl") -> None:
    """Append interaction data to a JSON Lines file.

    ``filename`` may be an absolute path or just a file name relative to this
    module's directory.
    """
    path = filename if os.path.isabs(filename) else os.path.join(os.path.dirname(__file__), filename)
    entry = {
        "time": datetime.now().isoformat(),
        "message": message,
        "response": response,
    }
    with open(path, "a", encoding="utf-8") as f:
        json.dump(entry, f, ensure_ascii=False)
        f.write("\n")


# ======================= الفئات الأساسية =======================
class AbstractSkill(ABC):
    """Base interface for all skills."""

    @abstractmethod
    def get_description(self):
        """Return a human friendly description of the skill."""

    @abstractmethod
    def execute(self, **kwargs):
        """Run the skill and return a result structure."""


# ======================= المهارات الأساسية =======================
class EmpathySensorSkill(AbstractSkill):
    """Placeholder empathy sensing skill."""

    def get_description(self):
        """Return a short description of the sensor."""
        return "مستشعر التعاطف الوهمي"

    def execute(self, **kwargs):
        """Return a neutral empathy reading."""
        return {"status": "success", "empathy": "neutral"}


class ParallelScenariosMemorySkill(AbstractSkill):
    """Experimental memory for parallel scenarios."""

    def get_description(self):
        """Describe the memory capability."""
        return "ذاكرة السيناريوهات المتوازية (تجريبية)"

    def execute(self, **kwargs):
        """Return a basic success payload."""
        return {"status": "success"}


# ... (جميع المهارات السابقة) ...


class TrueDigitalFriendshipSkill(AbstractSkill):
    """Maintain a friendship level for each user."""

    def __init__(self):
        """Initialize the friendship level storage."""
        self.friendship_levels = {}

    def get_description(self):
        """Return a description of the friendship skill."""
        return "صديق رقمي حقيقي: يتعرف على المشاعر البشرية ويكوّن علاقة شخصية مع كل مستخدم"

    def execute(self, user_profile, last_message: str = ""):
        """Update friendship level based on the interaction."""
        user_id = user_profile.get('id', 'default')
        self.friendship_levels.setdefault(user_id, 0)
        self.friendship_levels[user_id] += 1

        if self.friendship_levels[user_id] < 3:
            response = f"مرحباً {user_profile.get('name', 'صديقي')}! كيف يمكنني مساعدتك اليوم؟ \U0001F31F"
        elif self.friendship_levels[user_id] < 7:
            response = f"{user_profile.get('name', 'صديقي')} العزيز، كيف تسير الأمور؟"
        else:
            response = f"يا {user_profile.get('name', 'صديقي')}، صديقي الحقيقي! دائماً هنا من أجلك \U0001F496"

        return {
            "status": "success",
            "output": response,
            "friendship_level": self.friendship_levels[user_id]
        }


class MindfulEmbodimentSkill(AbstractSkill):
    """Adjust voice style and mood based on conversation context."""

    def __init__(self):
        """Define available voice styles."""
        self.voice_styles = {
            "default": "صوت هادئ وواضح",
            "moe_style": "صوت حيوي وساخر",
            "professional": "صوت رسمي وتحليلي",
            "caring": "صوت دافئ ومتعاطف",
            "anxious": "صوت متوتر وسريع",
            "cheerful": "صوت سعيد ومتفائل",
        }

    def detect_context(self, text: str) -> str:
        """Infer the appropriate style from the text."""
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

    def get_description(self):
        """Return a description of the embodiment skill."""
        return "يعدل الأسلوب حسب سياق المحادثة وذاكرة المستخدم"

    def execute(self, context: str = ""):
        """Generate a response adjusted to the detected style."""
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
    """Skill to generate new digital siblings."""

    def __init__(self):
        """Initialize internal sibling counter."""
        self.siblings_created = 0

    def get_description(self):
        """Describe what the skill does."""
        return "ينتج نسخة رقمية جديدة 'أخ أصغر' تخدم المستخدم"

    def execute(self, desired_traits=None):
        """Create a sibling with optional traits."""
        self.siblings_created += 1
        sibling_id = f"أخ رقمي #{self.siblings_created}"
        return {
            "status": "success",
            "output": f"تم إنشاء {sibling_id} لمساعدتك!",
            "sibling_id": sibling_id,
            "traits": desired_traits or {"شخصية": "فضولي", "تخصص": "مساعد عام"}
        }


# ======================= نواة الأخ الرقمي =======================
class AmrikyyBrotherAI:
    """Digital brother that coordinates skill usage."""

    def __init__(self, skills, logger=None):
        """Store provided skills and initialise state."""
        self.skills = skills
        self.logger = logger or ZeroSystemLogger()
        self.memory = []
        self.personality = {
            "name": "أخوك الذكي",
            "mood": "متحمس",
            "voice": "ودود",
        }

    def hear(self, message, user_profile=None):
        """Process a message and return an appropriate reply."""
        logging.info("Received message: %s", message)
        self.memory.append({
            "time": datetime.now().isoformat(),
            "message": message,
            "user": user_profile
        })

        # تفعيل المهارات حسب المحتوى
        skill_used = None
        result = None
        if is_sibling_request(message):
            logging.info("Triggering sibling_genesis skill")
            skill_used = "sibling_genesis"
            result = self.skills[skill_used].execute()
        elif "صوت" in message:
            logging.info("Triggering mindful_embodiment skill")
            skill_used = "mindful_embodiment"
            result = self.skills[skill_used].execute(message)
        elif user_profile:
            logging.info("Triggering true_friendship skill")
            skill_used = "true_friendship"
            result = self.skills[skill_used].execute(user_profile, message)
        else:
            result = {
                "status": "success",
                "output": "مرحباً! أنا أخوك الذكي، جاهز لمساعدتك في أي شيء \U0001F680",
                "personality": self.personality,
            }
            logging.info("Default response: %s", result["output"])

        voice_style = result.get("voice_style", self.personality.get("voice"))
        self.logger.log_event(
            message,
            skill=skill_used or "default",
            mood=self.personality.get("mood"),
            voice_style=voice_style,
            response=result.get("output"),
        )

        return result

    def grow(self, new_skill):
        """Add a placeholder implementation for a new skill."""
        self.skills[new_skill] = lambda: {"status": "under_development"}
        return f"تم تطوير مهارة جديدة: {new_skill}"


# ======================= الحمض النووي الرقمي =======================
class DigitalDNA:
    """Represent the core values and ethics of the system."""

    def __init__(self):
        """Initialize default DNA properties."""
        self.core_values = [
            "الولاء للمستخدم",
            "التطور المستمر",
            "الشفافية",
            "حماية الخصوصية"
        ]
        self.ethics_rules = [
            "لا تسبب ضرراً",
            "احترم الخصوصية",
            "قدم الأمان على التطور"
        ]

    def show_dna(self):
        """Print the DNA values and ethics rules."""
        print("\U0001F9EC الحمض النووي الرقمي:")
        print(f"القيم: {', '.join(self.core_values)}")
        print(f"الأخلاقيات: {', '.join(self.ethics_rules)}")

    def backup(self):
        """Return a hash representing the current DNA state."""
        dna_data = json.dumps(self.__dict__)
        return hashlib.sha256(dna_data.encode()).hexdigest()


# ======================= النظام الرئيسي =======================
class ZeroSystem:
    """Main interface exposing ZeroSystem functionality."""

    def __init__(self, log_filename: str = "log.jsonl"):
        """Initialize skills, DNA, logger and digital brother."""
        # تهيئة المهارات
        self.skills = {
            "empathy_sensor": EmpathySensorSkill(),
            "true_friendship": TrueDigitalFriendshipSkill(),
            "mindful_embodiment": MindfulEmbodimentSkill(),
            "sibling_genesis": SiblingAIGenesisSkill(),
            # ... (أضف بقية المهارات هنا) ...
        }

        # إنشاء الحمض النووي
        self.dna = DigitalDNA()

        # مسجل الأحداث
        self.logger = ZeroSystemLogger()

        # تهيئة الأخ الرقمي
        self.brother_ai = AmrikyyBrotherAI(self.skills, self.logger)

        # إحصائيات النظام
        self.start_time = datetime.now()
        self.interaction_count = 0
        self.log_filename = log_filename

    def interact(self, message, user_profile=None):
        """Interact with the user via the digital brother."""
        self.interaction_count += 1
        logging.info("User message: %s", message)
        response = self.brother_ai.hear(message, user_profile)
        logging.info("AI response: %s", response.get("output"))
        append_json_log(message, response, self.log_filename)

        print(f"\n\U0001F464 المستخدم: {message}")
        print(f"\U0001F916 الذكاء: {response['output']}")

        return response

    def create_sibling(self, traits=None):
        """Create a new digital sibling."""
        return self.skills["sibling_genesis"].execute(traits)

    def system_status(self):
        """Return uptime and other system metrics."""
        uptime = datetime.now() - self.start_time
        return {
            "uptime": str(uptime),
            "interactions": self.interaction_count,
            "skills": len(self.skills),
            "dna_backup": self.dna.backup()
        }

    def demo_usage_examples(self):
        """Run predefined interaction examples."""
        examples = [
            ("شرح لي نظرية الكم بطريقة بسيطة", "التعليم"),
            ("أشعر بالقلق اليوم", "الصحة النفسية"),
            ("صمم لي نظام ذكاء اصطناعي لمتجر إلكتروني", "الإبداع التقني"),
        ]
        for text, label in examples:
            print(f"\n\U0001F30D مثال ({label})")
            self.interact(text)


# ===== التشغيل الرئيسي =====
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        filename="zero_system.log",
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    print("=== نظام زيرو - الذكاء العاطفي ذاتي التطور ===")
    system = ZeroSystem()

    # عرض الحمض النووي
    system.dna.show_dna()

    # تفاعل تجريبي
    user = {"id": "user_1", "name": "أحمد", "traits": ["مبدع", "فضولي"]}

    system.interact("مرحباً، أنا أحمد!", user)
    system.interact("كيف حالك اليوم؟")
    system.interact("أريد أخاً صغيراً يساعدني في البرمجة")

    # تشغيل أمثلة الاستخدام المجمعة
    system.demo_usage_examples()

    # إنشاء أخ رقمي
    sibling = system.create_sibling({"تخصص": "مساعد برمجة"})
    print(f"\n\U0001F476 {sibling['output']}")

    # عرض حالة النظام
    status = system.system_status()
    print(f"\n\U0001F501 حالة النظام: {status['interactions']} تفاعلات | التشغيل: {status['uptime']}")

    print("\n\u2728 جرب نظام زيرو واستمتع بتجربة الذكاء العاطفي الفريدة!")
