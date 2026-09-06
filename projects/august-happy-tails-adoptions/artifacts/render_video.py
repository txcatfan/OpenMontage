import json
import os
import sys
from dotenv import load_dotenv

load_dotenv()
sys.path.insert(0, os.path.abspath("."))

from tools.video.video_compose import VideoCompose

def run():
    proj_dir = os.path.join(os.path.abspath("."), "projects", "august-happy-tails-adoptions")
    edit_decisions_path = os.path.join(proj_dir, "artifacts", "edit_decisions.json")
    asset_manifest_path = os.path.join(proj_dir, "artifacts", "asset_manifest.json")
    output_path = os.path.join(proj_dir, "renders", "happy_tails_august_sample_v4.mp4")

    with open(edit_decisions_path, "r", encoding="utf-8") as f:
        edit_decisions = json.load(f)

    with open(asset_manifest_path, "r", encoding="utf-8") as f:
        asset_manifest = json.load(f)

    print("Starting VideoCompose for Test Video #4...")
    print(f"Output: {output_path}")

    composer = VideoCompose()
    result = composer.execute({
        "operation": "render",
        "edit_decisions": edit_decisions,
        "asset_manifest": asset_manifest,
        "output_path": output_path
    })

    print("Compose finished!")
    print("Success:", result.success)
    if result.success:
        print("Output:", result.artifacts.get("output_path", output_path))
        print("Duration seconds:", result.duration_seconds)
    else:
        print("Error:", result.error)
        sys.exit(1)

if __name__ == "__main__":
    run()
