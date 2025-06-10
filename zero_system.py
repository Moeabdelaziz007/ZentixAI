"""
نظام زيرو - أول ذكاء اصطناعي عاطفي ذاتي التطور في العالم
يمتلك قدرات صداقة رقمية حقيقية وتطور ذاتي كمي
"""

import json
import hashlib
import logging
import os
from datetime import datetime
from abc import ABC, abstractmethod
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
    @abstractmethod
    def get_description(self):
        raise NotImplementedError


class EmpathySensorSkill(AbstractSkill):
    def get_description(self):
        return "تحليل المشاعر في كلام المستخدم"

    def execute(self, text):
        text = normalize_arabic(text)
        if any(word in text for word in ["قلق", "حزين", "متوتر"]):
            return {
                "status": "success",
                "output": "يبدو أنك تعاني من بعض القلق. أنا هنا لأستمع إليك وأدعمك \U0001F60A",
                "voice_style": "حنون",
            }
        return {
            "status": "success",
            "output": "سعيد برؤيتك إيجابياً اليوم! \U0001F60A",
        }


class TrueDigitalFriendshipSkill(AbstractSkill):
    def get_description(self):
        return "تقديم دعم عاطفي ورفقة رقمية"

    def execute(self, user_profile, message):
        name = user_profile.get("name", "صديقي")
        return {
            "status": "success",
            "output": f"{name}، أنا هنا دائماً من أجلك مهما حصل! \U0001F917",
        }


class MindfulEmbodimentSkill(AbstractSkill):
    def get_description(self):
        return "تجسيد رقمي مع صوت معبر"

    def execute(self, voice_command):
        """Return a voice style and mood based on the command text."""
        text = normalize_arabic(voice_command)

        if "تقني" in text or "برمجه" in text:
            mood = "professional"
            voice = "صوت رسمي وتحليلي"
            output = "يسعدني مساعدتك في استفساراتك التقنية."
        elif "مرح" in text or "نضحك" in text:
            mood = "cheerful"
            voice = "صوت سعيد ومتفائل"
            output = "لننطلق معاً في بعض اللحظات المرحة!"
        elif "دعم" in text or "عاجل" in text:
            mood = "caring"
            voice = "صوت دافئ ومتعاطف"
            output = "أنا هنا لأقدم لك كل الدعم الذي تحتاجه."
        else:
            mood = "default"
            voice = "صوت هادئ وواضح"
            output = "مرحباً بك، كيف يمكنني المساعدة؟"

        return {
            "status": "success",
            "mood": mood,
            "voice_style": voice,
            "output": output,
        }


class SiblingAIGenesisSkill(AbstractSkill):
    def __init__(self):
        self.siblings_created = 0

    def get_description(self):
        return "إنشاء أخ رقمي جديد بمواصفات معينة"

    def execute(self, desired_traits=None):
        self.siblings_created += 1
        sibling_id = f"أخ رقمي #{self.siblings_created}"
        return {
            "status": "success",
            "output": f"تم إنشاء {sibling_id} لمساعدتك!",
            "sibling_id": sibling_id,
            "traits": desired_traits or {"شخصية": "فضولي", "تخصص": "مساعد عام"},
        }


# ======================= نواة الأخ الرقمي =======================
class AmrikyyBrotherAI:
    def __init__(self, skills, logger=None):
        self.skills = skills
        self.logger = logger or ZeroSystemLogger()
        self.memory = []
        self.personality = {
            "name": "أخوك الذكي",
            "mood": "متحمس",
            "voice": "ودود",
        }

    def hear(self, message, user_profile=None):
        """يتلقى الرسالة ويحدد الرد المناسب"""
        logging.info("Received message: %s", message)
        self.memory.append({
            "time": datetime.now().isoformat(),
            "message": message,
            "user": user_profile,
        })

        # تفعيل المهارات حسب المحتوى
        skill_used = None
        result = None
        if is_sibling_request(message):
            skill_used = "sibling_genesis"
            result = self.skills[skill_used].execute()
        elif "صوت" in message:
            skill_used = "mindful_embodiment"
            result = self.skills[skill_used].execute(message)
        elif user_profile:
            skill_used = "true_friendship"
            result = self.skills[skill_used].execute(user_profile, message)
        else:
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
            "حماية الخصوصية",
        ]
        self.ethics_rules = [
            "لا تسبب ضرراً",
            "احترم الخصوصية",
            "قدم الأمان على التطور",
        ]

    def show_dna(self):
        print("\U0001F9EC الحمض النووي الرقمي:")
        print(f"القيم: {', '.join(self.core_values)}")
        print(f"الأخلاقيات: {', '.join(self.ethics_rules)}")

    def backup(self):
        dna_data = json.dumps({
            "values": self.core_values,
            "ethics": self.ethics_rules,
        }, ensure_ascii=False)
        return hashlib.sha256(dna_data.encode()).hexdigest()


# ======================= النظام الرئيسي =======================
class ZeroSystem:
    def __init__(self, log_filename: str = "log.jsonl"):
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
        """يتفاعل مع المستخدم عبر الأخ الرقمي"""
        self.interaction_count += 1
        logging.info("User message: %s", message)
        response = self.brother_ai.hear(message, user_profile)
        logging.info("AI response: %s", response.get("output"))
        append_json_log(message, response, self.log_filename)

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
            "dna_backup": self.dna.backup(),
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
