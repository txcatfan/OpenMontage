"""Generate Scene 5: Spooky Dracula with Cape (The Winner!)."""

import os
import sys
import json
import time
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(repo_root))

from tools.video.seedance_video import SeedanceVideo

prompt = """GLOBAL STYLE
  Cinematic live-action video, warm cozy retail interior, gentle depth of field, 16:9 widescreen, smooth photorealistic dog fur and fabric textures.

SCENE
  At the same Halloween costume boutique dressing room, Charlie the dachshund emerges wearing a magnificent Spooky Dracula vampire cape, looking thrilled, proud, and confident.

CHARACTERS
  Charlie is the dachshund from Reference 1: smooth reddish-tan coat, floppy hound ears with soft shading, expressive dark eyes, elongated dachshund body and short sturdy legs.
  Wardrobe: Charlie is wearing a handsome miniature Dracula vampire costume: a satin black cape with a standing crimson red collar tied with a small ribbon around his neck, flowing gracefully along his back.

LOCATION
  The exact same boutique dressing room area with rich dark red velvet curtains in the background and a soft beige carpeted floor.

FIRST FRAME AND BLOCKING
  The red velvet dressing room curtain parts. Charlie steps forward on all four paws into center frame, head held high.

ACTION & CAMERA
  Eye-level dog camera framing matching the series.
  Charlie struts out proudly from between the red velvet curtains into center frame. His black and red Dracula cape billows gently behind him. He stops center frame, puffs out his little chest, wags his tail happily, and looks directly into the camera with an alert, triumphant, joyful dog smile. He stays center stage looking dashing, striking a proud vampire pose.

OPTICS / CAMERA
  Low eye-level camera matching dachshund eye height, steady locked-off framing.

PHYSICS
  Confident proud dachshund strut, happy wagging tail, smooth satin fabric of the black and red vampire cape fluttering gently.

LIGHTING
  Warm boutique lighting, rich cinematic glow on the satin cape and his glossy reddish coat.

AUDIO
  Soft fabric rustle of velvet curtains parting, a gentle heroic cape swish, happy dog tail thump, cheerful breathing. No dialogue, no human speech.
"""

def main():
    tool = SeedanceVideo()
    ref_url = "https://v3b.fal.media/files/b/0aac91f6/RSyhXOzB9dwUQiKtJk-yK_charlie_reference_picture.jpg"
    output_video = str(repo_root / "projects" / "lonestar-doxietalk-halloween" / "assets" / "video" / "scene5_dracula_5s.mp4")

    inputs = {
        "prompt": prompt,
        "operation": "reference_to_video",
        "model_version": "2.5",
        "model_variant": "standard",
        "duration": "5",
        "aspect_ratio": "16:9",
        "resolution": "720p",
        "generate_audio": True,
        "reference_image_urls": [ref_url],
        "output_path": output_video,
    }

    print("Submitting Seedance 2.5 generation for Scene 5: Spooky Dracula...")
    print(f"Reference URL: {ref_url}")
    print(f"Output Video Path: {output_video}")
    result = tool.execute(inputs)
    print("Result success:", result.success)
    if not result.success:
        print("Error:", result.error)
    else:
        print(f"Saved Dracula video successfully to: {output_video}")
        print(f"Cost: ${result.cost_usd:.2f}, Duration: {result.duration_seconds}s")

if __name__ == "__main__":
    main()
