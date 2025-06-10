# ZentixAI

This repository demonstrates a minimal plugin-based system in Python along with a small web dashboard. The `plugin_example.py` file shows how to register and execute a calculator plugin, while `zero_system.py` contains an Arabic demo implementing a friendly digital assistant.

## Requirements

* Python 3.8 or later
* Only standard library modules are required

## Usage

Run the calculator plugin:

```bash
python plugin_example.py
# {'result': 8}
```

Launch the demo assistant:

```bash
python zero_system.py
```

Use the command line interface:

```bash
python cli.py interactive   # start an interactive chat session
python cli.py status        # display system status information
python cli.py demo          # run the predefined demo interactions
```

## Running Tests

Install `pytest` and execute:

```bash
pytest
```

The tests verify plugin behaviour and key `ZeroSystem` features.

## Web Dashboard

The provided Next.js template can be started with:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open <http://localhost:3000> in Onlook to view the dashboard.

## License

This project is licensed under the [MIT License](LICENSE).
