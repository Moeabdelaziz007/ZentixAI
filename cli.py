"""Simple command line interface for :mod:`zero_system`."""

import argparse
import logging
from zero_system import ZeroSystem


def print_zero_system_info() -> None:
    print(
        """
============================================
🧠  نظام زيرو (Zero System) — ذكاء عاطفي ذاتي التطور
--------------------------------------------
- أول ذكاء اصطناعي عاطفي ذاتي التطور في العالم
- يمتلك قدرات صداقة رقمية وتعلم ذاتي مستمر
--------------------------------------------

⭐️ أمثلة الاستخدام:
--------------------------
> التعليم:
system.interact("شرح لي نظرية الكم بطريقة بسيطة")
# 🤖 الذكاء: العالم مثل قطع ليغو صغيرة متداخلة...

> الصحة النفسية:
system.interact("أشعر بالقلق اليوم")
# 🤖 الذكاء: أفهم مشاعرك. خذ نفساً عميقاً معي... 💆‍♂️

> الإبداع التقني:
system.interact("صمم لي نظام ذكاء اصطناعي لمتجر إلكتروني")
# 🤖 الذكاء: أنشأت لك نظاماً بمواصفات: [التفاصيل]... هل تريد تعديلاً؟

--------------------------------------------
🖥️ أوامر CLI:
python cli.py interactive   # بدء جلسة محادثة
python cli.py status        # عرض حالة النظام
python cli.py demo          # تشغيل تفاعلات العرض التجريبي

--------------------------------------------
✅ اختبارات النظام (pytest):
python -m pytest

--------------------------------------------
👀 Onlook Dashboard:
http://localhost:3000

--------------------------------------------
🧑‍💻 متطلبات:
- Python 3.8+
- لا توجد اعتمادات خارجية

--------------------------------------------
🪪 الرخصة: MIT License

🚀 جرب نظام زيرو وشاركنا تجربتك!
============================================
"""
    )


def run_interactive(system: ZeroSystem) -> None:
    """Launch an interactive chat loop."""
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


def main(argv: list[str] | None = None) -> None:
    logging.basicConfig(
        level=logging.INFO,
        filename="zero_system.log",
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    parser = argparse.ArgumentParser(description="Zero System command line interface")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("interactive", help="start interactive session")
    sub.add_parser("status", help="print system status")
    sub.add_parser("demo", help="run predefined usage examples")
    sub.add_parser("info", help="print system summary")

    args = parser.parse_args(argv)

    system = ZeroSystem()

    if args.command == "interactive":
        run_interactive(system)
    elif args.command == "status":
        print(system.system_status())
    elif args.command == "demo":
        system.demo_usage_examples()
    elif args.command == "info":
        print_zero_system_info()


if __name__ == "__main__":
    main()
