"""Generate Scene 5 v3: Spooky Dracula with proportionate fangs and excited tail wag."""

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
  At the same Halloween costume boutique dressing room, Charlie the dachshund emerges wearing the handsome Spooky Dracula vampire costume from Reference 2, looking thrilled, proud, and smiling happily with his cute vampire fangs.

CHARACTERS
  Charlie is the dachshund from Reference 1: smooth reddish-tan coat, floppy hound ears with soft shading, expressive dark eyes, elongated dachshund body and short sturdy legs.
  Wardrobe: Charlie is wearing the exact Dracula vampire costume from Reference 2 (dracula_costume_reference.jpg): a black satin cape with a standing crimson red collar, a crisp red bowtie, little black vest with buttons, and two small, cute, realistic white vampire fangs neatly peeking over his lower lip as shown in Reference 2.

COUNT LOCK
  Two small, subtle, realistic canine vampire fangs only matching Reference 2. Never oversized tusks.

LOCATION
  The exact same boutique dressing room area with rich dark red velvet curtains in the background and a soft beige carpeted floor.

FIRST FRAME AND BLOCKING
  The red velvet dressing room curtain parts. Charlie steps forward on all four paws into center frame, head held high, already wearing his complete Dracula costume with his cute fangs.

ACTION & CAMERA
  Eye-level dog camera framing matching the series.
  Charlie struts out proudly from between the red velvet curtains into center frame wearing his black and red Dracula cape and bowtie. He stops center stage, puffs out his little chest proudly, wags his tail excitedly back and forth, and looks directly into the camera with a happy, beaming dog smile showing his cute little vampire fangs. He holds his proud, dashing vampire pose center stage looking joyful and festive.

OPTICS / CAMERA
  Low eye-level camera matching dachshund eye height, steady locked-off framing.

PHYSICS
  Confident proud dachshund strut, vigorous happy tail wagging back and forth, smooth satin fabric of the black and red cape moving with his body.

LIGHTING
  Warm boutique lighting, rich cinematic glow on the satin cape and his glossy reddish coat.

AUDIO
  Soft fabric rustle of velvet curtains parting, gentle cape movement, happy dog tail thumps, cheerful dog breathing. No dialogue, no human speech.
"""

def main():
    tool = SeedanceVideo()
    ref_charlie = str(repo_root / "projects" / "lonestar-doxietalk-halloween" / "assets" / "images" / "charlie_reference_picture.jpg")
    ref_dracula = str(repo_root / "projects" / "lonestar-doxietalk-halloween" / "assets" / "images" / "dracula_costume_reference.jpg")
    output_video = str(repo_root / "projects" / "lonestar-doxietalk-halloween" / "assets" / "video" / "scene5_dracula_winner_5s.mp4")

    inputs = {
        "prompt": prompt,
        "operation": "reference_to_video",
        "model_version": "2.5",
        "model_variant": "standard",
        "duration": "5",
        "aspect_ratio": "16:9",
        "resolution": "720p",
        "generate_audio": True,
        "reference_image_paths": [ref_charlie, ref_dracula],
        "output_path": output_video,
    }

    print("Submitting Seedance 2.5 generation for Scene 5 (Dracula Winner v3)...")
    print(f"Reference 1 (Charlie): {ref_charlie}")
    print(f"Reference 2 (Dracula): {ref_dracula}")
    print(f"Output Video Path: {output_video}")
    result = tool.execute(inputs)
    print("Result success:", result.success)
    if not result.success:
        print("Error:", result.error)
    else:
        print(f"Saved Dracula Winner video successfully to: {output_video}")
        print(f"Cost: ${result.cost_usd:.2f}, Duration: {result.duration_seconds}s")

if __name__ == "__main__":
    main()
