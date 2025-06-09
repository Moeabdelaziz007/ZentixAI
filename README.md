# sss

This repository demonstrates a minimal plugin-based system in Python. See `plugin_example.py` for a simple calculator plugin and how to invoke it. The `zero_system.py` script contains a larger Arabic demo that implements a friendly digital assistant.

Requires **Python&nbsp;3.10 or later**. No additional dependencies beyond the standard library are needed.

Run the calculator plugin directly:
```bash
python plugin_example.py
```
This prints `{'result': 8}`.

## Usage Examples

Run `python zero_system.py` to launch the demo. The script starts a simple
interactive text interface where you can chat with the assistant. To use the
system programmatically, instantiate `ZeroSystem` in your own code:

```python
from zero_system import ZeroSystem

system = ZeroSystem()
```

Below are sample interactions, retrieving the `"output"` field from each
response:

### التعليم
```python
resp = system.interact("شرح لي نظرية الكم بطريقة بسيطة")
resp["output"]
# 🤖 الذكاء: بالطبع! تخيل أن العالم مكون من قطع ليغو صغيرة...
```

### الصحة النفسية
```python
resp = system.interact("أشعر بالقلق اليوم")
resp["output"]
# 🤖 الذكاء: أتفهم شعورك، دعنا نتنفس معاً... 💆‍♂️
```

### الإبداع التقني
```python
resp = system.interact("صمم لي نظام ذكاء اصطناعي لمتجر إلكتروني")
resp["output"]
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
