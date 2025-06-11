# ZentixAI

This project showcases a minimal plugin-based framework in Python alongside a simple web dashboard built with Next.js, TailwindCSS and ShadCN. The `zero_system.py` script provides an Arabic demo of a friendly digital assistant, while `plugin_example.py` implements a calculator plugin.

## Usage

Run the calculator plugin directly:

```bash
python plugin_example.py
# {'result': 8}
```

Start the demo assistant:

```bash
python zero_system.py
```

Interact with the system through the command line interface:

```bash
python cli.py interactive   # start an interactive chat session
python cli.py status        # display system status information
python cli.py demo          # run the predefined demo interactions
```

## Web Dashboard

The Next.js dashboard can be launched with any package manager:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open <http://localhost:3000> in your browser to view the dashboard.

## Running Tests

This repository uses `pytest` for unit testing:

```bash
pytest
```

