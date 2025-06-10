  <<<<<<< codex/document-python-cli-options-and-test-suite
  """Command line interface for the Zero System."""

  import argparse

  from zero_system import ZeroSystem


  def interactive_mode(system: ZeroSystem) -> None:
      """Run the interactive chat loop."""
  =======
  import logging
  from zero_system import ZeroSystem


  def main():
      logging.basicConfig(
          level=logging.INFO,
          filename="zero_system.log",
          format="%(asctime)s - %(levelname)s - %(message)s",
      )
  >>>>>>> main
    print("=== Zero System CLI ===")
    system.dna.show_dna()
    try:
        while True:
            message = input("\U0001F464 المستخدم: ")
            if message.lower() in {"exit", "quit"}:
                break
            system.interact(message)
    except KeyboardInterrupt:
        pass


def show_status(system: ZeroSystem) -> None:
    """Display basic system statistics."""
    status = system.system_status()
    print("\U0001F4CA System status:")
    for key, value in status.items():
        print(f"{key}: {value}")


def show_dna(system: ZeroSystem) -> None:
    """Print the digital DNA description."""
    system.dna.show_dna()


def show_mood(system: ZeroSystem) -> None:
    """Display the current mood via the embodiment skill."""
    result = system.skills["mindful_embodiment"].execute()
    print("\U0001F4AD Current mood:", result["mood"])
    print(result["output"])


def main() -> None:
    parser = argparse.ArgumentParser(description="Zero System command line interface")
    parser.add_argument(
        "mode",
        nargs="?",
        default="interactive",
        choices=["interactive", "status", "dna", "mood"],
        help="operation mode",
    )
    args = parser.parse_args()

    system = ZeroSystem()

    if args.mode == "interactive":
        interactive_mode(system)
    elif args.mode == "status":
        show_status(system)
    elif args.mode == "dna":
        show_dna(system)
    elif args.mode == "mood":
        show_mood(system)


if __name__ == "__main__":
    main()
