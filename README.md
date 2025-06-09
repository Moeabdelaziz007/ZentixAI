# sss

This repository demonstrates a minimal plugin-based system in Python. See `plugin_example.py` for a simple calculator plugin and how to invoke it. The `zero_system.py` script contains a larger Arabic demo that implements a friendly digital assistant.

## Setup

The project only requires **Python&nbsp;3.8 or later** and uses no external packages beyond the standard library. No additional requirements need to be installed, and `requirements.txt` is intentionally empty.

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

This repository includes a small test suite in the `tests/` directory. The suite
uses only the standard library `unittest` module. From the repository root, run
all tests with:

```bash
python -m unittest discover -v
```

The tests verify the calculator plugin and the digital sibling creation logic.

## License

MIT License

Copyright (c) 2025 Mohamed H Abdelaziz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
