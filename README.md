# sss

This repository demonstrates a minimal plugin-based system in Python. See `plugin_example.py` for a simple calculator plugin and how to invoke it. The `zero_system.py` script contains a larger Arabic demo that implements a friendly digital assistant.

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
