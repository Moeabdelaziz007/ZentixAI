from __future__ import annotations

import json
import os
from datetime import datetime
from typing import Any, Dict, Optional

from logger import ZeroSystemLogger
from zero_system.learning.qlearn import QLearner


class AbstractSkill:
    def execute(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        raise NotImplementedError


class SiblingAIGenesisSkill(AbstractSkill):
    def __init__(self) -> None:
        self.siblings_created = 0

    def execute(self, traits: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        self.siblings_created += 1
        sid = f"أخ رقمي #{self.siblings_created}"
        return {
            "status": "success",
            "output": f"تم إنشاء {sid}!",
            "sibling_id": sid,
            "traits": traits or {"شخصية": "فضولي", "تخصص": "مساعد عام"},
        }


class TrueDigitalFriendshipSkill(AbstractSkill):
    def execute(self, user_profile: Optional[Dict[str, Any]] = None, message: str = "") -> Dict[str, Any]:
        name = (user_profile or {}).get("name", "صديقي")
        return {"status": "success", "output": f"مرحباً {name}!"}


class MindfulEmbodimentSkill(AbstractSkill):
    def execute(self, message: str = "") -> Dict[str, Any]:
        return {"status": "success", "output": "ها هو صوتك الافتراضي"}


def append_json_log(message: str, response: Dict[str, Any], filename: str = "log.jsonl") -> None:
    path = filename if os.path.isabs(filename) else os.path.join(os.path.dirname(__file__), filename)
    entry = {"time": datetime.now().isoformat(), "message": message, "response": response}
    with open(path, "a", encoding="utf-8") as f:
        json.dump(entry, f, ensure_ascii=False)
        f.write("\n")


class AmrikyyBrotherAI:
    def __init__(self, skills: Dict[str, AbstractSkill], logger: Optional[ZeroSystemLogger] = None) -> None:
        self.skills = skills
        self.logger = logger or ZeroSystemLogger()

    def hear(self, message: str, user_profile: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if "أخ" in message:
            skill = "sibling_genesis"
            result = self.skills[skill].execute()
        elif user_profile:
            skill = "true_friendship"
            result = self.skills[skill].execute(user_profile, message)
        else:
            skill = "default"
            result = {"status": "success", "output": "مرحباً! أنا أخوك الذكي."}
        result["skill"] = skill
        return result


class ZeroSystem:
    def __init__(self, log_filename: str = "log.jsonl") -> None:
        self.skills = {
            "sibling_genesis": SiblingAIGenesisSkill(),
            "true_friendship": TrueDigitalFriendshipSkill(),
            "mindful_embodiment": MindfulEmbodimentSkill(),
        }
        self.logger = ZeroSystemLogger()
        self.brother_ai = AmrikyyBrotherAI(self.skills, self.logger)
        self.learner = QLearner()
        self.log_filename = log_filename

    def interact(self, message: str, user_profile: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        response = self.brother_ai.hear(message, user_profile)
        append_json_log(message, response, self.log_filename)
        reward = 1.0 if response.get("status") == "success" else 0.0
        self.learner.update(str(message), str(response.get("skill")), reward, str(response.get("output")))
        return response
