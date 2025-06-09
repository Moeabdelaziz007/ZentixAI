
from zero_system import ZeroSystem
import argparse


def interactive_loop(system: ZeroSystem) -> None:
    """Run an interactive chat session."""
    system.dna.show_dna()
    try:
        while True:
            message = input("\U0001F464 المستخدم: ")
            if message.lower() in {"exit", "quit"}:
                break
            system.interact(message)
    except KeyboardInterrupt:
        pass


def main() -> None:
    parser = argparse.ArgumentParser(description="Zero System command line interface")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("interactive", help="Start interactive mode")
    subparsers.add_parser("status", help="Show system status")
    subparsers.add_parser("dna", help="Display digital DNA")
    subparsers.add_parser("mood", help="Show current AI mood")

    args = parser.parse_args()

    system = ZeroSystem()

    if args.command == "status":
        status = system.system_status()
        print(f"\U0001F501 حالة النظام: {status['interactions']} تفاعلات | التشغيل: {status['uptime']}")
    elif args.command == "dna":
        system.dna.show_dna()
    elif args.command == "mood":
        mood = system.brother_ai.personality.get("mood", "unknown")
        print(f"\U0001F60A المزاج الحالي: {mood}")
    else:
        # Default to interactive mode
        interactive_loop(system)


if __name__ == "__main__":
    main()
