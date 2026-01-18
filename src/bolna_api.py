import requests


def fetch_transcript(api_key: str, execution_id: str) -> str:
    url = f"https://api.bolna.ai/executions/{execution_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()

    data = response.json()
    transcript = data.get("transcript", "")
    if not transcript:
        raise ValueError("No transcript found in the API response")

    return transcript
