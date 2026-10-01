"""Run Seedance 2.5 reference-to-video generation for Charlie Halloween Costume Test 2: Texas Lone Star Cowboy."""

import os
import sys
import json
from pathlib import Path

# Ensure repo root is in python path
repo_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(repo_root))

from tools.video.seedance_video import SeedanceVideo

prompt = """GLOBAL STYLE
  Cinematic live-action video, warm cozy retail interior, gentle depth of field, 16:9 widescreen, smooth photorealistic dog fur and fabric textures.

SCENE
  At the same Halloween specialty store dressing room, Charlie the dachshund emerges wearing a Texas Lone Star Cowboy costume, looking skeptical and unimpressed.

CHARACTERS
  Charlie is the dachshund from the reference turnaround sheet: smooth reddish-tan coat, floppy hound ears with soft shading, expressive dark eyes, elongated dachshund body and short sturdy legs. He is wearing a miniature brown felt Texas cowboy hat sitting neatly between his hound ears and a bright red paisley cowboy bandana neatly tied around his neck.

LOCATION
  The exact same boutique dressing room area with rich dark red velvet curtains in the background and a soft beige carpeted floor.

FIRST FRAME AND BLOCKING
  The red velvet dressing room curtain parts. Charlie steps forward on all four paws into center frame, facing forward.

ACTION & CAMERA
  Eye-level dog camera framing matching the first scene.
  Charlie steps out from between the red velvet curtains into center frame wearing his miniature Texas cowboy hat and red bandana. He pauses center frame, looks directly at the camera with an unamused, skeptical expression, blinking slowly. He then turns around in an arc and trots deliberately back inside behind the red velvet curtains.

OPTICS / CAMERA
  Low eye-level camera matching dachshund eye height, steady locked-off framing.

PHYSICS
  Natural dachshund walking gait, soft ear bounce under the cowboy hat brim as he turns, little bandana gently fluttering with his steps.

LIGHTING
  Warm boutique lighting, soft highlights on his reddish coat.

AUDIO
  Soft fabric rustle of velvet curtains parting, tiny dog paws softly on carpet, a quiet gentle dog snort or sigh. No dialogue, no human speech.
"""

def main():
    tool = SeedanceVideo()
    ref_image = str(repo_root / "projects" / "lonestar-doxietalk-halloween" / "assets" / "images" / "charlie_reference_picture.jpg")
    output_video = str(repo_root / "projects" / "lonestar-doxietalk-halloween" / "assets" / "video" / "test_cowboy_5s.mp4")

    inputs = {
        "prompt": prompt,
        "operation": "reference_to_video",
        "model_version": "2.5",
        "model_variant": "standard",
        "duration": "5",
        "aspect_ratio": "16:9",
        "resolution": "720p",
        "generate_audio": True,
        "reference_image_paths": [ref_image],
        "output_path": output_video,
    }

    print("Submitting Seedance 2.5 reference-to-video generation for Texas Cowboy...")
    print(f"Reference Image: {ref_image}")
    print(f"Output Video Path: {output_video}")
    result = tool.execute(inputs)
    print("Result success:", result.success)
    if not result.success:
        print("Error:", result.error)
    else:
        print("Data:", json.dumps(result.data, indent=2))
        print(f"Cost: ${result.cost_usd:.2f}, Duration: {result.duration_seconds}s")

if __name__ == "__main__":
    main()
