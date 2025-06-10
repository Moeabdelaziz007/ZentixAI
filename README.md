# Onlook Starter Template

<p align="center">
  <img src="app/favicon.ico" />
</p>

This is an [Onlook](https://onlook.com/) project set up with
[Next.js](https://nextjs.org/), [TailwindCSS](https://tailwindcss.com/) and
[ShadCN](https://ui.shadcn.com).

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

## Python Components

Several utilities and a basic dashboard are written in Python. The examples below
assume you are using a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### CLI

Run the interactive command line interface:

```bash
python cli.py
```

### Flask dashboard

Start the login-protected chat dashboard with:

```bash
python dashboard.py
```

It will run on `http://localhost:5000` by default.

### HTTP dashboard server

To serve the static dashboard and expose `status.json`, run:

```bash
python dashboard_server.py
```

### Running tests

Execute the test suite using [`pytest`](https://docs.pytest.org/):

```bash
pytest
```
