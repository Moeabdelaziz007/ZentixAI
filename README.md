# Onlook Starter Template

<p align="center">
  <img src="app/favicon.ico" />
</p>

This is an [Onlook](https://onlook.com/) project set up with
[Next.js](https://nextjs.org/), [TailwindCSS](https://tailwindcss.com/) and
[ShadCN](https://ui.shadcn.com).

## Getting Started

1. **Start the Next.js development server**

   ```bash
   npm run dev
   # or
   yarn dev
   # or
   pnpm dev
   # or
   bun dev
   ```

   Then open [http://localhost:3000](http://localhost:3000) in Onlook.

2. **Use the Python CLI** (requires **Python 3.10+** since union types are used
   in `cli.py` and `plugin_example.py`)

   ```bash
   python cli.py interactive  # start an interactive chat session
   python cli.py status       # display system status information
   python cli.py demo         # run the predefined demo interactions
   ```

## Running Tests

This repository uses `pytest` for unit testing. From the repository root run:

```bash
pytest
```

The tests in `tests/test_zero_system.py` verify that sibling requests are
detected correctly, that the system status includes expected fields, and that
creating siblings produces unique identifiers.
