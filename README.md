# sss

This repository demonstrates a minimal plugin-based system in Python. See `plugin_example.py` for a simple calculator plugin and how to invoke it. The `zero_system.py` script contains a larger Arabic demo that implements a friendly digital assistant.

Requires **Python&nbsp;3.10 or later**. No additional dependencies beyond the standard library are needed.

Run the calculator plugin directly:
```bash
python plugin_example.py
```
This prints `{'result': 8}`.

## Command Line Interface

`cli.py` exposes a small interface for the main system. Choose one of the
following modes:

```bash
python cli.py [interactive|status|dna|mood]
```

- `interactive` – start an interactive chat session (default)
- `status` – display basic system statistics
- `dna` – print the digital DNA information
- `mood` – show the current mood as detected by the embodiment skill

## Usage Examples

Run `python zero_system.py` to launch the demo and create a `system` object. Below are sample interactions with the system:

### التعليم
```python
system.interact("شرح لي نظرية الكم بطريقة بسيطة")
# 🤖 الذكاء: بالطبع! تخيل أن العالم مكون من قطع ليغو صغيرة...
```

### الصحة النفسية
```python
system.interact("أشعر بالقلق اليوم")
# 🤖 الذكاء: أتفهم شعورك، دعنا نتنفس معاً... 💆‍♂️
```

### الإبداع التقني
```python
system.interact("صمم لي نظام ذكاء اصطناعي لمتجر إلكتروني")
# 🤖 الذكاء: أنشأت لك نظاماً بمواصفات: [التفاصيل]... هل تريد تعديلاً؟
```

## Running Tests

This repository includes a small test suite in the `tests/` directory. To run
all tests, execute:

```bash
pytest -v
```

The tests verify the calculator plugin and the digital sibling creation logic
and are implemented using the `unittest` framework, so `python -m unittest`
will also work.

## License

Distributed under the [MIT License](LICENSE).
