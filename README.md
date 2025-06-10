# Onlook Starter Template

<p align="center">
  <img src="app/favicon.ico" />
</p>

This is an [Onlook](https://onlook.com/) project set up with [Next.js](https://nextjs.org/), [TailwindCSS](https://tailwindcss.com/) and [ShadCN](https://ui.shadcn.com).

Run the calculator plugin directly:
```bash
python plugin_example.py
```
This prints `{'result': 8}`.

## Usage Examples

Run `python zero_system.py` to launch the demo and create a `system` object. Here are some example interactions:

### الإبداع التقني
```python
system.interact("صمم لي نظام ذكاء اصطناعي لمتجر إلكتروني")
# 🤖 الذكاء: أنشأت لك نظاماً بمواصفات: [التفاصيل]... هل تريد تعديلاً؟
```

## Command Line Interface

Use `cli.py` to interact with the system from the terminal. The script exposes a few simple commands:

```bash
python cli.py interactive   # start an interactive chat session
python cli.py status        # display system status information
python cli.py demo          # run the predefined demo interactions
```

## Running Tests

This repository uses `pytest` for unit testing. From the repository root run:

```bash
pytest
```

The tests in `tests/test_zero_system.py` verify that sibling requests are detected correctly, that the system status includes expected fields, and that creating siblings produces unique identifiers.

Open [http://localhost:3000](http://localhost:3000) in Onlook to see the result.
