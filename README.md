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

