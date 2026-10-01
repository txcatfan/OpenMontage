"""Poll and save the cleaned multi-reference Seedance 2.5 Hot Dog v2 generation."""

import os
import sys
import time
import requests
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(repo_root))

from tools.base_tool import _load_dotenv
_load_dotenv()

api_key = os.environ.get("FAL_KEY")
headers = {"Authorization": f"Key {api_key}"}

request_id = "01a0f50b-df66-7d23-9df5-8b76d1f1bcd1"
status_url = f"https://queue.fal.run/bytedance/seedance-2.5/requests/{request_id}/status"
response_url = f"https://queue.fal.run/bytedance/seedance-2.5/requests/{request_id}"
output_path = repo_root / "projects" / "lonestar-doxietalk-halloween" / "assets" / "video" / "test_hotdog_v2_5s.mp4"

print(f"Polling Seedance 2.5 request {request_id}...")

while True:
    time.sleep(5)
    resp = requests.get(status_url, headers=headers, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    status = data.get("status", "UNKNOWN")
    print(f"Status: {status}")
    if status == "COMPLETED":
        break
    if status in ("FAILED", "CANCELLED"):
        print("Generation failed:", data)
        sys.exit(1)

# Fetch final result
result_resp = requests.get(response_url, headers=headers, timeout=30)
result_resp.raise_for_status()
res_data = result_resp.json()

video_url = res_data["video"]["url"]
print(f"Downloading video from {video_url}...")
v_resp = requests.get(video_url, timeout=120)
v_resp.raise_for_status()

output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_bytes(v_resp.content)
print(f"Saved video successfully to {output_path} ({len(v_resp.content)} bytes)")
