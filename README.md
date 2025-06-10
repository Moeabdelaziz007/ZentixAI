# Onlook Starter Template

<p align="center">
  <img src="app/favicon.ico" />
</p>

This is an [Onlook](https://onlook.com/) project set up with
[Next.js](https://nextjs.org/), [TailwindCSS](https://tailwindcss.com/) and
[ShadCN](https://ui.shadcn.com).

## Getting Started

### Next.js development server

Run the development server:

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

### Command Line Interface

This project also includes a simple command-line interface for the `ZeroSystem`.
It requires **Python 3.10+** as union type syntax is used in `cli.py` and
`plugin_example.py`.

Use `cli.py` to interact with the system from the terminal:

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

The tests in `tests/test_zero_system.py` verify that sibling requests are
detected correctly, that the system status includes expected fields, and that
creating siblings produces unique identifiers.
