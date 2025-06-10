import logging
from .zero_system import ZeroSystem


def main():
    logging.basicConfig(
        level=logging.INFO,
        filename="zero_system.log",
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    print("=== Zero System CLI ===")
    system = ZeroSystem()
    system.dna.show_dna()
    try:
        while True:
            message = input("\U0001F464 المستخدم: ")
            if message.lower() in {"exit", "quit"}:
                break
            system.interact(message)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
