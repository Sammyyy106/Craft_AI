# CraftAI Assignment

## Project Overview
This project processes and extracts information from an input dataset and provides parsing and API helper utilities. The repository contains code to extract, parse, and (optionally) expose data via a wrapper API.

## Contents
- [main.py](main.py) — entry point for running the project.
- [requirements.txt](requirements.txt) — Python dependencies.
- [extracted_data.csv](extracted_data.csv) — example output or input data file.
- [src/](src/) — package containing core modules:
  - [src/bolna_api.py](src/bolna_api.py) — API wrapper/helper functions.
  - [src/config.py](src/config.py) — configuration values and constants.
  - [src/extractor.py](src/extractor.py) — data extraction logic.
  - [src/parsers.py](src/parsers.py) — parsing utilities.

## Setup
1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

## Usage
- To run the main script:

```powershell
python main.py
```

- If `main.py` expects arguments or configuration, see `src/config.py` for configurable settings.

## Development
- To explore extraction logic, open `src/extractor.py`.
- To modify parsers, see `src/parsers.py`.
- To adapt API helpers, see `src/bolna_api.py`.

## Project Structure
A short overview of responsibilities:
- `main.py` orchestrates the run flow.
- `src/extractor.py` reads and transforms raw input.
- `src/parsers.py` contains functions to parse and normalize fields.
- `src/config.py` stores environment/config variables.
- `src/bolna_api.py` contains convenience functions to interact with external services (if used).

## Notes
- Ensure `requirements.txt` is up-to-date before running.
- If the project needs environment variables, add them to `src/config.py` or use an `.env` file as appropriate.

## License & Contact
Include an appropriate license if you plan to share this repository. For questions, contact the repository owner.
