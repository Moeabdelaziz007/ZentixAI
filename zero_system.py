"""
Zero System - the world's first self-evolving emotional AI.
It offers genuine digital friendship and continuous self-growth.
"""

import json
import hashlib
from datetime import datetime
from abc import ABC, abstractmethod


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


# ======================= Core Classes =======================
class AbstractSkill(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def execute(self, **kwargs):
        pass


# ======================= Core Skills =======================
class EmpathySensorSkill(AbstractSkill):
    def get_description(self):
        return "Imaginary empathy sensor"

    def execute(self, **kwargs):
        # Returns a neutral empathy reading as a placeholder
        return {"status": "success", "empathy": "neutral"}


class ParallelScenariosMemorySkill(AbstractSkill):
    def get_description(self):
        return "Parallel scenarios memory (experimental)"

    def execute(self, **kwargs):
        return {"status": "success"}


# ... (all previous skills) ...


class TrueDigitalFriendshipSkill(AbstractSkill):
    def __init__(self):
        self.friendship_levels = {}

    def get_description(self):
        return (
            "True digital friendship: recognizes human emotions and builds a "
            "personal relationship with each user"
        )

    def execute(self, user_profile, last_message=""):
        user_id = user_profile.get('id', 'default')
        self.friendship_levels.setdefault(user_id, 0)
        self.friendship_levels[user_id] += 1

        if self.friendship_levels[user_id] < 3:
            response = (
                f"Hello {user_profile.get('name', 'friend')}! How can I help you today? \U0001F31F"
            )
        elif self.friendship_levels[user_id] < 7:
            response = f"Dear {user_profile.get('name', 'friend')}, how are things going?"
        else:
            response = (
                f"Hey {user_profile.get('name', 'friend')}, my true friend! Always here for you \U0001F496"
            )

        return {
            "status": "success",
            "output": response,
            "friendship_level": self.friendship_levels[user_id]
        }


class MindfulEmbodimentSkill(AbstractSkill):
    def __init__(self):
        self.voice_styles = {
            "default": "Calm and clear voice",
            "moe_style": "Energetic and playful voice",
            "professional": "Formal, analytical voice",
            "caring": "Warm and empathetic voice",
        }

    def get_description(self):
        return "Adjusts tone based on context and user memory"

    def execute(self, context=""):
        if "technical question" in context:
            style = "professional"
        elif "support" in context:
            style = "caring"
        elif "fun" in context:
            style = "moe_style"
        else:
            style = "default"

        responses = {
            "default": "Hello, how can I help you?",
            "moe_style": "Boss! Ready for any crazy idea \U0001F604",
            "professional": "Greetings, I'm ready for your technical questions",
            "caring": "I'm here for you. How can I assist today?",
        }

        return {
            "status": "success",
            "output": responses[style],
            "voice_style": self.voice_styles[style]
        }


class SiblingAIGenesisSkill(AbstractSkill):
    def __init__(self):
        self.siblings_created = 0

    def get_description(self):
        return "Generates a new digital 'little brother' to assist the user"

    def execute(self, desired_traits=None):
        self.siblings_created += 1
        sibling_id = f"Digital brother #{self.siblings_created}"
        return {
            "status": "success",
            "output": f"Created {sibling_id} to assist you!",
            "sibling_id": sibling_id,
            "traits": desired_traits or {"personality": "curious", "specialty": "general helper"}
        }


# ======================= Digital Brother Core =======================
class AmrikyyBrotherAI:
    def __init__(self, skills):
        self.skills = skills
        self.memory = []
        self.personality = {
            "name": "Smart Brother",
            "mood": "excited",
            "voice": "friendly",
        }

    def hear(self, message, user_profile=None):
        """Receive a message and determine an appropriate reply"""
        self.memory.append({
            "time": datetime.now().isoformat(),
            "message": message,
            "user": user_profile
        })

        # Activate skills based on message content
        if is_sibling_request(message):
            return self.skills["sibling_genesis"].execute()
        if "voice" in message:
            return self.skills["mindful_embodiment"].execute(message)
        if user_profile:
            return self.skills["true_friendship"].execute(user_profile, message)

        # Default reply
        return {
            "status": "success",
            "output": "Hello! I'm your smart brother, ready to help with anything \U0001F680",
            "personality": self.personality
        }

    def grow(self, new_skill):
        """Develop a new skill"""
        self.skills[new_skill] = lambda: {"status": "under_development"}
        return f"New skill developed: {new_skill}"


# ======================= Digital DNA =======================
class DigitalDNA:
    def __init__(self):
        self.core_values = [
            "Loyalty to the user",
            "Continuous growth",
            "Transparency",
            "Privacy protection",
        ]
        self.ethics_rules = [
            "Do no harm",
            "Respect privacy",
            "Prioritize safety over growth",
        ]

    def show_dna(self):
        print("\U0001F9EC Digital DNA:")
        print(f"Values: {', '.join(self.core_values)}")
        print(f"Ethics: {', '.join(self.ethics_rules)}")

    def backup(self):
        dna_data = json.dumps(self.__dict__)
        return hashlib.sha256(dna_data.encode()).hexdigest()


# ======================= Main System =======================
class ZeroSystem:
    def __init__(self):
        # Initialize skills
        self.skills = {
            "empathy_sensor": EmpathySensorSkill(),
            "true_friendship": TrueDigitalFriendshipSkill(),
            "mindful_embodiment": MindfulEmbodimentSkill(),
            "sibling_genesis": SiblingAIGenesisSkill(),
            # ... (add more skills here) ...
        }

        # Create the digital DNA
        self.dna = DigitalDNA()

        # Initialize the digital brother
        self.brother_ai = AmrikyyBrotherAI(self.skills)

        # System statistics
        self.start_time = datetime.now()
        self.interaction_count = 0

    def interact(self, message, user_profile=None):
        """Interact with the user through the digital brother AI"""
        self.interaction_count += 1
        response = self.brother_ai.hear(message, user_profile)

        print(f"\n\U0001F464 User: {message}")
        print(f"\U0001F916 AI: {response['output']}")

        return response

    def create_sibling(self, traits=None):
        """Create a new digital sibling"""
        return self.skills["sibling_genesis"].execute(traits)

    def system_status(self):
        """Show system status"""
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
            ("Explain quantum theory in simple terms", "Education"),
            ("I feel anxious today", "Mental health"),
            ("Design an AI system for an online store", "Technical creativity"),
        ]
        for text, label in examples:
            print(f"\n\U0001F30D Example ({label})")
            self.interact(text)


# ===== Main Execution =====
if __name__ == "__main__":
    print("=== Zero System - self-evolving emotional AI ===")
    system = ZeroSystem()

    # Show the digital DNA
    system.dna.show_dna()

    # Demo interactions
    user = {"id": "user_1", "name": "Ahmed", "traits": ["creative", "curious"]}

    system.interact("Hello, I'm Ahmed!", user)
    system.interact("How are you today?")
    system.interact("I want a little brother to help me with programming")

    # Run the predefined usage examples
    system.demo_usage_examples()

    # Create a digital sibling
    sibling = system.create_sibling({"specialty": "programming assistant"})
    print(f"\n\U0001F476 {sibling['output']}")

    # Show system status
    status = system.system_status()
    print(f"\n\U0001F501 System status: {status['interactions']} interactions | uptime: {status['uptime']}")

    print("\n\u2728 Try Zero System and enjoy the unique emotional AI experience!")
