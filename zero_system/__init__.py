"""ZeroSystem Quantum AI Agent"""
import json
import os
import logging
from datetime import datetime
from typing import Any, Dict, Optional

from logger import ZeroSystemLogger
from zero_system.skills.empathy_sensor import EmpathySensorSkill
from zero_system.skills.parallel_memory import ParallelScenariosMemorySkill
from zero_system.skills.true_friendship import TrueDigitalFriendshipSkill
from zero_system.skills.mindful_embodiment import MindfulEmbodimentSkill
from zero_system.skills.sibling_genesis import SiblingAIGenesisSkill
from zero_system.learning.qlearn import QLearningAgent
from zero_system.plugins.registry import PluginRegistry


def append_json_log(message: str, response: Dict[str, Any], filename: str = "log.jsonl") -> None:
    path = filename if os.path.isabs(filename) else os.path.join(os.path.dirname(__file__), filename)
    entry = {"time": datetime.now().isoformat(), "message": message, "response": response}
    with open(path, "a", encoding="utf-8") as f:
        json.dump(entry, f, ensure_ascii=False)
        f.write("\n")


def normalize_arabic(text: str) -> str:
    replacements = {"أ": "ا", "إ": "ا", "آ": "ا", "ى": "ي", "ة": "ه"}
    for src, target in replacements.items():
        text = text.replace(src, target)
    return text


def is_sibling_request(text: str) -> bool:
    norm = normalize_arabic(text)
    has_brother = any(t in norm for t in ["اخ", "شقيق"])
    has_small = any(t in norm for t in ["صغير", "اصغر"])
    return has_brother and has_small


class AmrikyyBrotherAI:
    def __init__(self, skills: Dict[str, Any], logger: Optional[ZeroSystemLogger] = None):
        self.skills = skills
        self.logger = logger or ZeroSystemLogger()
        self.memory = []
        self.mood_history = []

    def record_mood(self, mood: str) -> None:
        self.mood_history.append((datetime.now(), mood))
        self.mood_history = self.mood_history[-100:]

    def get_mood_history(self, n: int = 10):
        return self.mood_history[-n:]

    def hear(self, message: str, user_profile: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        logging.info("Received message: %s", message)
        result: Dict[str, Any]
        if is_sibling_request(message):
            result = self.skills["sibling_genesis"].execute()
        elif "صوت" in message:
            result = self.skills["mindful_embodiment"].execute(message)
        elif user_profile:
            result = self.skills["true_friendship"].execute(user_profile, message)
        else:
            result = {"status": "success", "output": "مرحباً! أنا أخوك الذكي."}
        mood = result.get("mood")
        if mood:
            self.record_mood(mood)
        self.logger.log_event(
            message,
            skill=result.get("skill"),
            mood=mood,
            voice_style=result.get("voice_style"),
            response=result.get("output"),
        )
        return result


class ZeroSystem:
    def __init__(self, log_filename: str = "log.jsonl", plugin_dir: str = "plugins"):
        self.skills = {
            "empathy_sensor": EmpathySensorSkill(),
            "true_friendship": TrueDigitalFriendshipSkill(),
            "mindful_embodiment": MindfulEmbodimentSkill(),
            "sibling_genesis": SiblingAIGenesisSkill(),
            "parallel_memory": ParallelScenariosMemorySkill(),
        }
        self.dna = {"values": ["الولاء للمستخدم", "التطور المستمر", "الشفافية"], "ethics": ["لا تسبب ضرراً"]}
        self.logger = ZeroSystemLogger()
        self.brother_ai = AmrikyyBrotherAI(self.skills, self.logger)
        self.learning = QLearningAgent()
        self.start_time = datetime.now()
        self.interaction_count = 0
        self.log_filename = log_filename
        PluginRegistry.load_plugins(plugin_dir)

    def interact(self, message: str, user_profile: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        self.interaction_count += 1
        response = self.brother_ai.hear(message, user_profile)
        append_json_log(message, response, self.log_filename)
        return response

    def execute_plugin(self, name: str, inputs: Dict[str, Any]) -> Dict[str, Any]:
        plugin = PluginRegistry.get(name)
        if not plugin:
            raise ValueError(f"No plugin named '{name}' registered")
        return plugin.execute(inputs)

    def get_mood_history(self, n: int = 10):
        return self.brother_ai.get_mood_history(n)

    def system_status(self) -> Dict[str, Any]:
        uptime = datetime.now() - self.start_time
        return {
            "uptime": str(uptime),
            "interactions": self.interaction_count,
            "skills": list(self.skills.keys()),
        }

__all__ = [
    "ZeroSystem",
    "AmrikyyBrotherAI",
    "PluginRegistry",
    "EmpathySensorSkill",
    "TrueDigitalFriendshipSkill",
    "MindfulEmbodimentSkill",
    "SiblingAIGenesisSkill",
    "ParallelScenariosMemorySkill",
    "QLearningAgent",
]
