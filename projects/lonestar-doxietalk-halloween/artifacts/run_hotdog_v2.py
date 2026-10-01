"""Run Seedance 2.5 multi-reference video generation for Charlie Hot Dog Costume v2."""

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
  Charlie is the dachshund from Reference 1 (charlie_reference_picture.jpg): smooth reddish-tan coat, floppy hound ears with soft shading, expressive dark eyes, elongated dachshund body and short sturdy legs.
  Wardrobe: Charlie is wearing the exact two-piece plush hot dog costume from Reference 2 (hotdog_costume_reference.jpg). The costume consists of two plush bun cushions fitted along his left and right flanks, a central red frankfurter sausage running along the top of his spine with a wavy yellow mustard line, secured by black harness straps.

COUNT LOCK
  Strictly two bun halves only (one left bun, one right bun flanking his body). One red sausage down the spine. Never a third bun, no extra rear cushion, no rear bread loaf. His hindquarters and tail are completely free as shown in Reference 2.

LOCATION
  A boutique dressing room area with rich dark red velvet curtains in the background and a soft beige carpeted floor.

FIRST FRAME AND BLOCKING
  The red velvet dressing room curtain parts. Charlie steps forward on all fours into center frame, facing forward.

ACTION & CAMERA
  Eye-level dog camera framing matching the series.
  Charlie steps out from between the red velvet curtains into center frame wearing the two-piece plush hot dog costume. He pauses center frame, stares straight into the camera with an unamused, deadpan expression, then turns around in an arc displaying only the two side buns and his back, and trots deliberately back inside behind the red velvet curtains.

OPTICS / CAMERA
  Low eye-level camera matching dachshund eye height, steady locked-off framing.

PHYSICS
  Natural dachshund walking gait, soft ear bounce as he turns, plush fabric bun cushions gently moving with his body.

LIGHTING
  Warm boutique lighting, soft highlights on his reddish coat.

AUDIO
  Soft fabric rustle of velvet curtains, tiny dog paws softly on carpet, a quiet little dog sigh. No dialogue, no human speech.
"""

def main():
    tool = SeedanceVideo()
    ref_charlie = str(repo_root / "projects" / "lonestar-doxietalk-halloween" / "assets" / "images" / "charlie_reference_picture.jpg")
    ref_costume = str(repo_root / "projects" / "lonestar-doxietalk-halloween" / "assets" / "images" / "hotdog_costume_reference.jpg")
    output_video = str(repo_root / "projects" / "lonestar-doxietalk-halloween" / "assets" / "video" / "test_hotdog_v2_5s.mp4")

    inputs = {
        "prompt": prompt,
        "operation": "reference_to_video",
        "model_version": "2.5",
        "model_variant": "standard",
        "duration": "5",
        "aspect_ratio": "16:9",
        "resolution": "720p",
        "generate_audio": True,
        "reference_image_paths": [ref_charlie, ref_costume],
        "output_path": output_video,
    }

    print("Submitting Seedance 2.5 multi-reference video generation (v2)...")
    print(f"Reference 1 (Charlie): {ref_charlie}")
    print(f"Reference 2 (Costume): {ref_costume}")
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
