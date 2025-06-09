# sss

This repository demonstrates a minimal plugin-based system in Python. See `plugin_example.py` for a simple calculator plugin and how to invoke it. The `zero_system.py` script contains a larger Arabic demo that implements a friendly digital assistant.

Run the calculator plugin directly:
```bash
python plugin_example.py
```
This prints `{'result': 8}`.

## Usage Examples

Install the optional [`rich`](https://github.com/Textualize/rich) library for a
text user interface:
```bash
pip install rich
```
Run `python zero_system.py` to launch the demo and create a `system` object.
Below are sample interactions with the system:

### التعليم
```python
print(system.interact("شرح لي نظرية الكم بطريقة بسيطة")["output"])
# 🤖 الذكاء: بالطبع! تخيل أن العالم مكون من قطع ليغو صغيرة...
```

### الصحة النفسية
```python
print(system.interact("أشعر بالقلق اليوم")["output"])
# 🤖 الذكاء: أتفهم شعورك، دعنا نتنفس معاً... 💆‍♂️
```

### الإبداع التقني
```python
print(system.interact("صمم لي نظام ذكاء اصطناعي لمتجر إلكتروني")["output"])
# 🤖 الذكاء: أنشأت لك نظاماً بمواصفات: [التفاصيل]... هل تريد تعديلاً؟
```

Every interaction is recorded to `zero_system.log` in JSON format.
