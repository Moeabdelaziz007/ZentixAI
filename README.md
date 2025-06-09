# sss

This repository demonstrates a minimal plugin-based system in Python. See `plugin_example.py` for a simple calculator plugin and how to invoke it. The `zero_system.py` script contains a larger Arabic demo that implements a friendly digital assistant.

## Setup

The project only requires **Python&nbsp;3.8 or later** and uses no external packages beyond the standard library.

1. Clone this repository.
2. *(Optional)* Create and activate a virtual environment.
3. Run any of the example scripts:
   ```bash
   python plugin_example.py
   python zero_system.py
   python cli.py
   ```

Run the calculator plugin directly:
```bash
python plugin_example.py
```
This prints `{'result': 8}`.

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
python -m unittest discover -v
```

The tests verify the calculator plugin and the digital sibling creation logic.

## License

Distributed under the [MIT License](LICENSE).
