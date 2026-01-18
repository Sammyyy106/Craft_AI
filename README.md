# CraftAI Assignment

## Project Overview
This repository extracts information from a Bolna AI voice-agent conversation and writes structured results to a CSV file. The code uses an execution ID from Bolna AI call history to fetch the conversation data, parse relevant fields, and append them to `extracted_data.csv`.

## Key Features
- Fetch conversation data from Bolna AI using an execution ID.
- Parse and normalize fields with `src/parsers.py`.
- Extract and transform data in `src/extractor.py`.
- Optional helper functions for API interactions in `src/bolna_api.py`.

## Contents
- [main.py](main.py) — entry point to run the extraction for a given execution ID.
- [requirements.txt](requirements.txt) — Python dependencies.
- [extracted_data.csv](extracted_data.csv) — resulting CSV where rows are appended.
- [src/](src/) — package modules:
  - [src/bolna_api.py](src/bolna_api.py)
  - [src/config.py](src/config.py)
  - [src/extractor.py](src/extractor.py)
  - [src/parsers.py](src/parsers.py)

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

3. Configure API credentials (if required):
- Check `src/config.py` for any API keys or endpoints. You may set environment variables or update the config file as appropriate.

## Usage
Run the project with an execution ID copied from Bolna AI call history. The script will fetch the conversation for that execution and append extracted fields to `extracted_data.csv`.

Example:

```powershell
python main.py --execution_id "3e5d887f-3838-46f4-be1a-bcef4aaaee51"
```

Notes:
- The `--execution_id` argument is required to fetch a specific conversation run.
- If the project requires additional flags (e.g., `--output` or log level), run `python main.py --help` to see available options.

## Output
- `extracted_data.csv` will contain one or more new rows corresponding to the fetched conversation. Column names and ordering are defined by the parsing logic in `src/parsers.py`.

## Development
- Inspect and modify extraction rules in `src/extractor.py`.
- Update field parsing and normalization in `src/parsers.py`.
- For Bolna-specific API calls, see `src/bolna_api.py` and `src/config.py` for endpoints and credentials.

## Troubleshooting
- If fetching fails, ensure API credentials and endpoints in `src/config.py` are correct and network access is available.
- If `extracted_data.csv` does not update, check for exceptions printed to console and run with increased logging.
- Use `python main.py --help` for CLI options and usage.

## License & Contact
Add a license if you plan to share this repository. For questions about this project, contact the repository owner.
