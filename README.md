# sss

This repository demonstrates a minimal plugin-based system in Python. See `plugin_example.py` for a simple calculator plugin and how to invoke it. The `zero_system.py` script contains a larger Arabic demo that implements a friendly digital assistant.

## Setup

The core examples run on **Python&nbsp;3.8 or later** and rely only on the standard library.
To use the optional Flask dashboard you will need to install the `flask` package.

1. Clone this repository.
2. *(Optional)* Create and activate a virtual environment.
3. Run any of the example scripts:
   ```bash
   python plugin_example.py
   python zero_system.py
   python cli.py
   ```
4. *(Optional)* Launch the Flask dashboard:
   ```bash
   python dashboard.py
   ```
   The templates directory and the `static/` folder with CSS should be
   placed beside `dashboard.py`.
   The default stylesheet uses neon green and medium gray on a dark
   background. The layout mimics the OpenAI chat interface with a
   scrollable chat area and a message input at the bottom.
   Edit `static/styles.css` to customize the theme.

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
