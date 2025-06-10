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
    """Append interaction data to a JSON Lines file."""
    path = os.path.join(os.path.dirname(__file__), filename)
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
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def execute(self, **kwargs):
        pass


# ======================= المهارات الأساسية =======================
class EmpathySensorSkill(AbstractSkill):
    def get_description(self):
        return "مستشعر التعاطف الوهمي"

    def execute(self, **kwargs):
        # Returns a neutral empathy reading as a placeholder
        return {"status": "success", "empathy": "neutral"}


class ParallelScenariosMemorySkill(AbstractSkill):
    def get_description(self):
        return "ذاكرة السيناريوهات المتوازية (تجريبية)"

    def execute(self, **kwargs):
        return {"status": "success"}


# ... (جميع المهارات السابقة) ...


class TrueDigitalFriendshipSkill(AbstractSkill):
    def __init__(self):
        self.friendship_levels = {}

    def get_description(self):
        return "صديق رقمي حقيقي: يتعرف على المشاعر البشرية ويكوّن علاقة شخصية مع كل مستخدم"

    def execute(self, user_profile, last_message=""):
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

    def get_description(self):
        return "يعدل الأسلوب حسب سياق المحادثة وذاكرة المستخدم"

    def execute(self, context: str = ""):
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
    def __init__(self):
        self.siblings_created = 0

    def get_description(self):
        return "ينتج نسخة رقمية جديدة 'أخ أصغر' تخدم المستخدم"

    def execute(self, desired_traits=None):
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
    def __init__(self, skills):
        self.skills = skills
        self.memory = []
        self.personality = {
            "name": "أخوك الذكي",
            "mood": "متحمس",
            "voice": "ودود"
        }

    def hear(self, message, user_profile=None):
        """يتلقى الرسالة ويحدد الرد المناسب"""
        logging.info("Received message: %s", message)
        self.memory.append({
            "time": datetime.now().isoformat(),
            "message": message,
            "user": user_profile
        })

        # تفعيل المهارات حسب المحتوى
        if is_sibling_request(message):
            logging.info("Triggering sibling_genesis skill")
            return self.skills["sibling_genesis"].execute()
        if "صوت" in message:
            logging.info("Triggering mindful_embodiment skill")
            return self.skills["mindful_embodiment"].execute(message)
        if user_profile:
            logging.info("Triggering true_friendship skill")
            return self.skills["true_friendship"].execute(user_profile, message)

        # الرد الافتراضي
        response = {
            "status": "success",
            "output": "مرحباً! أنا أخوك الذكي، جاهز لمساعدتك في أي شيء \U0001F680",
            "personality": self.personality
        }
        logging.info("Default response: %s", response["output"])
        return response

    def grow(self, new_skill):
        """يطور مهارة جديدة"""
        self.skills[new_skill] = lambda: {"status": "under_development"}
        return f"تم تطوير مهارة جديدة: {new_skill}"


# ======================= الحمض النووي الرقمي =======================
class DigitalDNA:
    def __init__(self):
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
        print("\U0001F9EC الحمض النووي الرقمي:")
        print(f"القيم: {', '.join(self.core_values)}")
        print(f"الأخلاقيات: {', '.join(self.ethics_rules)}")

    def backup(self):
        dna_data = json.dumps(self.__dict__)
        return hashlib.sha256(dna_data.encode()).hexdigest()


# ======================= النظام الرئيسي =======================
class ZeroSystem:
    def __init__(self):
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

        # تهيئة الأخ الرقمي
        self.brother_ai = AmrikyyBrotherAI(self.skills)

        # إحصائيات النظام
        self.start_time = datetime.now()
        self.interaction_count = 0

    def interact(self, message, user_profile=None):
        """يتفاعل مع المستخدم عبر الأخ الرقمي"""
        self.interaction_count += 1
        logging.info("User message: %s", message)
        response = self.brother_ai.hear(message, user_profile)
        logging.info("AI response: %s", response.get("output"))
        append_json_log(message, response)

        print(f"\n\U0001F464 المستخدم: {message}")
        print(f"\U0001F916 الذكاء: {response['output']}")

        return response

    def create_sibling(self, traits=None):
        """ينشئ أخاً رقمياً جديداً"""
        return self.skills["sibling_genesis"].execute(traits)

    def system_status(self):
        """يعرض حالة النظام"""
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
