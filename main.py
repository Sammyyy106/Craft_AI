import os
import argparse
import csv
from dotenv import load_dotenv

from src.bolna_api import fetch_transcript
from src.extractor import extract_from_transcript

load_dotenv()  # Load .env file

def main():
    parser = argparse.ArgumentParser(description="Bolna Call Transcript Extractor")
    parser.add_argument("--output_csv", default="extracted_data.csv",
                        help="Output CSV filename")
    parser.add_argument("--debug", action="store_true",
                        help="Show debug messages during extraction")
    parser.add_argument("--execution_id", type=str,
                        help="Bolna execution ID (optional - can enter interactively)")

    args = parser.parse_args()

    # Get API key from .env
    api_key = os.getenv("BOLNA_API_KEY")
    if not api_key:
        print("Error: BOLNA_API_KEY not found in .env file")
        return

    # Get execution ID — interactive if not provided
    execution_id = args.execution_id
    if not execution_id:
        execution_id = input("Enter Bolna Execution ID: ").strip()
        if not execution_id:
            print("No execution ID provided. Exiting.")
            return

    print(f"Fetching transcript for execution: {execution_id}")

    try:
        transcript = fetch_transcript(api_key, execution_id)
        extracted = extract_from_transcript(transcript, debug=args.debug)

        # Prepare CSV row - convert None/empty values to empty strings
        csv_row = {
            "loan_type": extracted.get("loan_type", ""),
            "monthly_income": extracted.get("monthly_income") if extracted.get("monthly_income") is not None else "",
            "source_of_income": extracted.get("source_of_income", ""),
            "address": extracted.get("address", ""),
            "pincode": extracted.get("pincode", "")
        }

        with open(args.output_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["loan_type", "monthly_income", "source_of_income", "address", "pincode"]
            )
            writer.writeheader()
            writer.writerow(csv_row)

        print("\n" + "="*60)
        print("CSV successfully generated:", args.output_csv)
        print("Extracted data:")
        for k, v in csv_row.items():
            try:
                print(f"  {k:18}: {v}")
            except UnicodeEncodeError:
                # Handle encoding issues on Windows console
                safe_v = str(v).encode('ascii', 'replace').decode('ascii')
                print(f"  {k:18}: {safe_v}")
        print("="*60 + "\n")

    except Exception as e:
        print(f"Error occurred: {str(e)}")


if __name__ == "__main__":
    main()
