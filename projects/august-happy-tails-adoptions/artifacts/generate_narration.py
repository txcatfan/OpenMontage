import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()

def generate_v4_audio():
    script_path = os.path.join("projects", "august-happy-tails-adoptions", "artifacts", "august_sample_script.md")
    with open(script_path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    voice_id = os.getenv("CHARLIE_VOICE_ID", "GdPqjbdsuwHYqzHrC45c")
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        print("ERROR: Missing ELEVENLABS_API_KEY")
        sys.exit(1)

    out_path = os.path.join("projects", "august-happy-tails-adoptions", "assets", "audio", "august_happy_tails_sample_v4_eleven_v3.mp3")

    print(f"Generating Eleven v3 TTS with voice_id={voice_id}...")
    print(f"Model: eleven_v3, Stability: 0.55, Format: mp3_44100_128")
    print("Script character length:", len(text))

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg",
    }
    payload = {
        "text": text,
        "model_id": "eleven_v3",
        "voice_settings": {
            "stability": 0.55,
        },
    }
    params = {
        "output_format": "mp3_44100_128"
    }

    resp = requests.post(url, headers=headers, json=payload, params=params, timeout=180)
    if resp.status_code != 200:
        print("ElevenLabs API Error:", resp.status_code, resp.text)
        sys.exit(1)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(resp.content)

    file_size_kb = len(resp.content) / 1024
    char_count = len(text)
    cost = round(char_count * 0.0003, 4)

    print("Success!")
    print(f"Output saved to: {out_path}")
    print(f"Size: {file_size_kb:.1f} KB, Characters: {char_count}, Estimated cost: ${cost:.4f}")

if __name__ == "__main__":
    generate_v4_audio()
