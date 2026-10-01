"""Run Kling video generation for Charlie Halloween Costume Tests 1 & 2."""

import os
import sys
import json
from pathlib import Path

# Ensure repo root is in python path
repo_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(repo_root))

from tools.video.kling_video import KlingVideo

def run_kling_job(name, start_frame_rel, prompt, output_rel):
    tool = KlingVideo()
    start_frame = str(repo_root / start_frame_rel)
    output_path = str(repo_root / output_rel)

    inputs = {
        "prompt": prompt,
        "operation": "image_to_video",
        "model_variant": "v3/standard",
        "duration": "5",
        "aspect_ratio": "16:9",
        "image_path": start_frame,
        "output_path": output_path,
    }

    print(f"\n==========================================")
    print(f"Running Kling job: {name}")
    print(f"Start Frame: {start_frame}")
    print(f"Output Video: {output_path}")
    print(f"Prompt: {prompt}")
    print(f"==========================================")

    result = tool.execute(inputs)
    print("Result success:", result.success)
    if not result.success:
        print("Error:", result.error)
    else:
        print(f"Output saved to: {result.data.get('output_path')}")
        print(f"Cost: ${result.cost_usd:.2f}, Duration: {result.duration_seconds}s")
    return result

def main():
    # 1. Hot Dog test
    prompt_hotdog = (
        "The dachshund in the plush hot dog costume pauses center frame, looks directly at the camera with an unamused, "
        "deadpan expression, then turns around in an arc, showing the hot dog bun and mustard squiggle on his back, "
        "and waddles back through the opening of the red velvet dressing room curtains. Smooth cinematic motion, low eye-level camera."
    )
    res1 = run_kling_job(
        "Kling Classic Hot Dog",
        "projects/lonestar-doxietalk-halloween/assets/images/hotdog_frames/frame_1s.jpg",
        prompt_hotdog,
        "projects/lonestar-doxietalk-halloween/assets/video/kling_test_hotdog_5s.mp4"
    )

    # 2. Texas Cowboy test
    prompt_cowboy = (
        "The dachshund in the miniature brown Texas cowboy hat and red bandana pauses center frame, looks directly at the camera "
        "with a skeptical deadpan expression, then turns around in an arc and waddles back through the opening of the red velvet "
        "dressing room curtains. Smooth cinematic motion, low eye-level camera."
    )
    res2 = run_kling_job(
        "Kling Texas Cowboy",
        "projects/lonestar-doxietalk-halloween/assets/images/cowboy_frames/frame_1s.jpg",
        prompt_cowboy,
        "projects/lonestar-doxietalk-halloween/assets/video/kling_test_cowboy_5s.mp4"
    )

    print("\nAll Kling test runs completed.")

if __name__ == "__main__":
    main()
