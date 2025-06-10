# Onlook Starter Template

<p align="center">
  <img src="app/favicon.ico" />
</p>

This is an [Onlook](https://onlook.com/) project set up with [Next.js](https://nextjs.org/), [TailwindCSS](https://tailwindcss.com/) and [ShadCN](https://ui.shadcn.com).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) in Onlook to see the result.

### Calculator Plugin

* Requires **Python 3.8 or later**
* No additional dependencies beyond the standard library

Run the calculator plugin directly:

```bash
python plugin_example.py
```

### الإبداع التقني
```python
system.interact("صمم لي نظام ذكاء اصطناعي لمتجر إلكتروني")
# 🤖 الذكاء: أنشأت لك نظاماً بمواصفات: [التفاصيل]... هل تريد تعديلاً؟
```

## Command Line Interface

Use `cli.py` to interact with the system from the terminal. The script exposes a few simple commands:

```bash
# start an interactive chat session
python cli.py interactive

# display system status information
python cli.py status

# run the predefined demo interactions
python cli.py demo
```

## Running Tests

This repository uses `pytest` for unit testing. From the repository root run:

```bash
pytest
```

The tests in `tests/test_zero_system.py` verify that sibling requests are detected correctly, that the system status includes expected fields, and that creating siblings produces unique identifiers.

