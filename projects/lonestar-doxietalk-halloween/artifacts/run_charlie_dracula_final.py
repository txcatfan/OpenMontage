"""Generate Scene 5: Charlie the Red Dachshund in Spooky Dracula Costume with cute fangs."""

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
  At the same boutique dressing room, Charlie the dachshund emerges wearing his handsome Spooky Dracula vampire costume, looking thrilled and proud, smiling with his cute little white vampire fangs and wagging his tail excitedly.

CHARACTERS
  Charlie is the dachshund from Reference 1 and Reference 2: smooth solid reddish-tan coat, subtle silver snout and whisker hairs, floppy hound ears, expressive dark eyes, elongated dachshund body and short sturdy legs. (Solid red/tan dachshund, matching all dressing room scenes).
  Wardrobe: Charlie is wearing the handsome Dracula costume shown in Reference 2: black satin cape with a tall standing crimson red collar, rich red bowtie, and satin vest.
  Face & Expression: Charlie has two small, delicate, proportionate white canine vampire fangs neatly peeking over his lower lip as shown in Reference 2. He is beaming with a proud, happy dog smile.

COUNT LOCK
  Solid reddish-tan coat only. Exactly two small, subtle, realistic canine vampire fangs neatly visible over the lower lip matching Reference 2. Never oversized tusks.

LOCATION
  The exact same boutique dressing room area with rich dark red velvet curtains in the background and a soft beige carpeted floor.

FIRST FRAME AND BLOCKING
  The red velvet dressing room curtain parts. Charlie steps forward on all four paws into center frame, head held high, wearing his Dracula cape, vest, and bowtie with his cute little fangs visible.

ACTION & CAMERA
  Eye-level dog camera framing matching the series.
  Charlie struts out proudly from between the red velvet curtains into center frame. He stops center stage, puffs out his little chest, wags his tail excitedly back and forth, and looks directly into the camera with a happy, beaming dog smile showing his cute little white vampire fangs. He holds his proud, dashing vampire pose center stage looking joyful and festive.

OPTICS / CAMERA
  Low eye-level camera matching dachshund eye height, steady locked-off framing.

PHYSICS
  Confident proud dachshund strut, vigorous happy tail wagging back and forth, smooth satin fabric of the black and red cape moving with his body.

LIGHTING
  Warm boutique lighting, rich cinematic glow on the satin cape and his glossy reddish coat.

AUDIO
  Soft fabric rustle of velvet curtains parting, gentle cape movement, happy dog tail thumps on carpet, cheerful dog breathing. No dialogue, no human speech.
"""

def main():
    tool = SeedanceVideo()
    ref_charlie = str(repo_root / "projects" / "lonestar-doxietalk-halloween" / "assets" / "images" / "charlie_reference_picture.jpg")
    ref_dracula = str(repo_root / "projects" / "lonestar-doxietalk-halloween" / "assets" / "images" / "charlie_dracula_fangs_reference.jpg")
    output_video = str(repo_root / "projects" / "lonestar-doxietalk-halloween" / "assets" / "video" / "scene5_dracula_final_5s.mp4")

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

    print("Submitting Seedance 2.5 generation for Charlie Dracula Final with Fangs...")
    print(f"Reference 1 (Charlie Turnaround): {ref_charlie}")
    print(f"Reference 2 (Charlie Dracula with Fangs): {ref_dracula}")
    print(f"Output Video Path: {output_video}")
    result = tool.execute(inputs)
    print("Result success:", result.success)
    if not result.success:
        print("Error:", result.error)
    else:
        print(f"Saved Charlie Dracula video successfully to: {output_video}")
        print(f"Cost: ${result.cost_usd:.2f}, Duration: {result.duration_seconds}s")

if __name__ == "__main__":
    main()
