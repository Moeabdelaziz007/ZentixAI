"""Core module for the ZeroSystem emotional AI."""

from datetime import datetime
import json
import hashlib
import logging
import os

from logger import ZeroSystemLogger
from skills import (
    AbstractSkill,
    EmpathySensorSkill,
    TrueDigitalFriendshipSkill,
    MindfulEmbodimentSkill,
    SiblingAIGenesisSkill,
    ParallelScenariosMemorySkill,
)


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
    """Detect if the user is requesting a younger digital sibling."""
    norm = normalize_arabic(text)
    has_brother = any(term in norm for term in ["اخ", "شقيق"])
    has_small = any(term in norm for term in ["صغير", "اصغر"])
    return has_brother and has_small


def append_json_log(message: str, response: dict, filename: str = "log.jsonl") -> None:
    """Append interaction data to a JSON Lines file."""
    path = filename if os.path.isabs(filename) else os.path.join(os.path.dirname(__file__), filename)
    entry = {"time": datetime.now().isoformat(), "message": message, "response": response}
    with open(path, "a", encoding="utf-8") as f:
        json.dump(entry, f, ensure_ascii=False)
        f.write("\n")


class AmrikyyBrotherAI:
    """The conversational core that routes messages to skills."""

    def __init__(self, skills: dict[str, AbstractSkill], logger: ZeroSystemLogger | None = None):
        self.skills = skills
        self.logger = logger or ZeroSystemLogger()
        self.memory = []
        self.personality = {"name": "أخوك الذكي", "mood": "متحمس", "voice": "ودود"}

    def hear(self, message: str, user_profile: dict | None = None):
        logging.info("Received message: %s", message)
        self.memory.append({"time": datetime.now().isoformat(), "message": message, "user": user_profile})
        skill_used = "default"
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
            logging.info("Default response")
            result = {
                "status": "success",
                "output": "مرحباً! أنا أخوك الذكي، جاهز لمساعدتك في أي شيء \U0001f680",
                "personality": self.personality,
            }

        voice_style = result.get("voice_style", self.personality.get("voice"))
        self.logger.log_event(
            message,
            skill=skill_used,
            mood=result.get("mood", self.personality.get("mood")),
            voice_style=voice_style,
            response=result.get("output"),
        )
        self.logger.log_mood(result.get("mood", self.personality.get("mood")))
        return result

    def grow(self, new_skill: str):
        """Dynamically register a placeholder skill."""
        self.skills[new_skill] = lambda: {"status": "under_development"}
        return f"تم تطوير مهارة جديدة: {new_skill}"


class DigitalDNA:
    """Represents the ethical core of the system."""

    def __init__(self):
        self.core_values = ["الولاء للمستخدم", "التطور المستمر", "الشفافية", "حماية الخصوصية"]
        self.ethics_rules = ["لا تسبب ضرراً", "احترم الخصوصية", "قدم الأمان على التطور"]

    def show_dna(self) -> None:
        print("\U0001F9EC الحمض النووي الرقمي:")
        print(f"القيم: {', '.join(self.core_values)}")
        print(f"الأخلاقيات: {', '.join(self.ethics_rules)}")

    def backup(self) -> str:
        dna_data = json.dumps(self.__dict__)
        return hashlib.sha256(dna_data.encode()).hexdigest()


class ZeroSystem:
    """Main facade that exposes skill functionality."""

    def __init__(self, log_filename: str = "log.jsonl"):
        self.skills = {
            "empathy_sensor": EmpathySensorSkill(),
            "true_friendship": TrueDigitalFriendshipSkill(),
            "mindful_embodiment": MindfulEmbodimentSkill(),
            "sibling_genesis": SiblingAIGenesisSkill(),
            "parallel_memory": ParallelScenariosMemorySkill(),
        }
        self.dna = DigitalDNA()
        self.logger = ZeroSystemLogger()
        self.brother_ai = AmrikyyBrotherAI(self.skills, self.logger)
        self.start_time = datetime.now()
        self.interaction_count = 0
        self.log_filename = log_filename

    def interact(self, message: str, user_profile: dict | None = None):
        self.interaction_count += 1
        logging.info("User message: %s", message)
        response = self.brother_ai.hear(message, user_profile)
        logging.info("AI response: %s", response.get("output"))
        append_json_log(message, response, self.log_filename)
        print(f"\n\U0001F464 المستخدم: {message}")
        print(f"\U0001F916 الذكاء: {response['output']}")
        return response

    def create_sibling(self, traits: dict | None = None):
        return self.skills["sibling_genesis"].execute(traits)

    def system_status(self) -> dict:
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
    logging.basicConfig(
        level=logging.INFO,
        filename="zero_system.log",
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    print("=== نظام زيرو - الذكاء العاطفي ذاتي التطور ===")
    system = ZeroSystem()

    system.dna.show_dna()

    user = {"id": "user_1", "name": "أحمد", "traits": ["مبدع", "فضولي"]}

    system.interact("مرحباً، أنا أحمد!", user)
    system.interact("كيف حالك اليوم؟")
    system.interact("أريد أخاً صغيراً يساعدني في البرمجة")

    system.demo_usage_examples()

    sibling = system.create_sibling({"تخصص": "مساعد برمجة"})
    print(f"\n\U0001F476 {sibling['output']}")

    status = system.system_status()
    print(
        f"\n\U0001F501 حالة النظام: {status['interactions']} تفاعلات | التشغيل: {status['uptime']}"
    )

    print("\n\u2728 جرب نظام زيرو واستمتع بتجربة الذكاء العاطفي الفريدة!")
