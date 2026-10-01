"""Run Seedance 2.5 reference-to-video generation for Charlie Halloween Costume Test 1: Classic Hot Dog."""

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
  At a Halloween specialty store dressing room, Charlie the dachshund emerges wearing a plush Hot Dog costume, looking totally unimpressed.

CHARACTERS
  Charlie is the dachshund from the reference turnaround sheet: smooth reddish-tan coat, floppy hound ears with soft shading, expressive dark eyes, elongated dachshund body and short sturdy legs. He is wearing a plush hot dog bun costume strapped over his back with a yellow wavy mustard line down the middle.

LOCATION
  A boutique dressing room area with rich dark red velvet curtains in the background and a soft carpeted floor.

FIRST FRAME AND BLOCKING
  The velvet dressing room curtain parts. Charlie steps forward on all fours into center frame, facing forward.

ACTION & CAMERA
  Eye-level dog camera framing.
  Charlie steps out from behind the curtain into center frame wearing the plush hot dog costume. He pauses center frame, stares straight into the camera with an unamused, deadpan expression, then turns around displaying the hot dog bun on his back, and trots deliberately back inside behind the velvet curtain.

OPTICS / CAMERA
  Low eye-level camera matching dachshund eye height, steady locked-off framing.

PHYSICS
  Natural dachshund walking gait, soft ear bounce as he turns, plush fabric bun gently moving with his body.

LIGHTING
  Warm boutique lighting, soft highlights on his reddish coat.

AUDIO
  Soft fabric rustle of velvet curtains, tiny dog paws softly on carpet, a quiet little dog sigh. No dialogue, no human speech.
"""

def main():
    tool = SeedanceVideo()
    ref_image = str(repo_root / "projects" / "lonestar-doxietalk-halloween" / "assets" / "images" / "charlie_reference_picture.jpg")
    output_video = str(repo_root / "projects" / "lonestar-doxietalk-halloween" / "assets" / "video" / "test_hotdog_5s.mp4")

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

    print("Submitting Seedance 2.5 reference-to-video generation...")
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
