# sss

This repository demonstrates a minimal plugin-based system in Python. See `plugin_example.py` for a simple calculator plugin and how to invoke it. The `zero_system.py` script contains a larger Arabic demo that implements a friendly digital assistant.

Run the calculator plugin directly:
```bash
python plugin_example.py
```
This prints `{'result': 8}`.

## Usage Examples

Run `python zero_system.py` to launch the demo and create a `system` object. Here are some example interactions:

### Education
```python
system.interact("Explain quantum theory in simple terms")
# 🤖 Assistant: Sure! Imagine the world is made of tiny Lego blocks...
```

### Mental health
```python
system.interact("I feel anxious today")
# 🤖 Assistant: I understand. Let's take a deep breath together... 💆‍♂️
```

### Technical creativity
```python
system.interact("Design an AI system for an online store")
# 🤖 Assistant: I've drafted a system with the following features... Need any adjustments?
```

For better results, pass a user profile dictionary with an `id` and `name` to
`interact()` so the assistant can remember you. You can also call
`system.demo_usage_examples()` to see these examples automatically.
