"""Generate the final 3 Charlie Halloween costume clips using Seedance 2.5."""

import os
import sys
import json
import time
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(repo_root))

from tools.video.seedance_video import SeedanceVideo

ref_charlie = str(repo_root / "projects" / "lonestar-doxietalk-halloween" / "assets" / "images" / "charlie_reference_picture.jpg")

jobs = [
    {
        "id": "scene3_pumpkin",
        "title": "Scene 3: Jack-O'-Lantern Pumpkin Suit (Fail)",
        "output": str(repo_root / "projects" / "lonestar-doxietalk-halloween" / "assets" / "video" / "scene3_pumpkin_5s.mp4"),
        "prompt": """GLOBAL STYLE
  Cinematic live-action video, warm cozy retail interior, gentle depth of field, 16:9 widescreen, smooth photorealistic dog fur and fabric textures.

SCENE
  At the same Halloween costume boutique dressing room, Charlie the dachshund emerges wearing a plush Jack-O-Lantern pumpkin suit, looking totally unimpressed.

CHARACTERS
  Charlie is the dachshund from Reference 1: smooth reddish-tan coat, floppy hound ears with soft shading, expressive dark eyes, elongated dachshund body and short sturdy legs.
  Wardrobe: Charlie is wearing a round orange plush Jack-O-Lantern pumpkin costume around his body, with a smiling black jack-o-lantern face pattern embroidered on the chest, and a green leafy collar around his neck.

COUNT LOCK
  Single orange pumpkin vest around his torso. His front and hind paws, face, ears, and tail remain completely visible and unencumbered.

LOCATION
  The exact same boutique dressing room area with rich dark red velvet curtains in the background and a soft beige carpeted floor.

FIRST FRAME AND BLOCKING
  The red velvet dressing room curtain parts. Charlie steps forward on all four paws into center frame, facing forward.

ACTION & CAMERA
  Eye-level dog camera framing matching the series.
  Charlie steps out from between the red velvet curtains into center frame wearing his round pumpkin suit. He pauses center frame, stares straight into the camera with an unamused, deadpan expression, blinking slowly. He then turns around in an arc and trots deliberately back inside behind the red velvet curtains.

OPTICS / CAMERA
  Low eye-level camera matching dachshund eye height, steady locked-off framing.

PHYSICS
  Natural dachshund walking gait, soft ear bounce as he turns, plush pumpkin fabric gently moving with his body.

LIGHTING
  Warm boutique lighting, soft highlights on his reddish coat.

AUDIO
  Soft fabric rustle of velvet curtains parting, tiny dog paws softly on carpet, a quiet gentle dog sigh. No dialogue, no human speech.
"""
    },
    {
        "id": "scene4_ghost",
        "title": "Scene 4: Bed-Sheet Ghost Costume (Fail)",
        "output": str(repo_root / "projects" / "lonestar-doxietalk-halloween" / "assets" / "video" / "scene4_ghost_5s.mp4"),
        "prompt": """GLOBAL STYLE
  Cinematic live-action video, warm cozy retail interior, gentle depth of field, 16:9 widescreen, smooth photorealistic dog fur and fabric textures.

SCENE
  At the same Halloween costume boutique dressing room, Charlie the dachshund emerges draped in a bed-sheet ghost costume with eye and ear cutouts, looking completely unimpressed.

CHARACTERS
  Charlie is the dachshund from Reference 1: smooth reddish-tan coat, floppy hound ears, expressive dark eyes, elongated dachshund body and short sturdy legs.
  Wardrobe: Charlie is wearing a funny homemade-style white bedsheet ghost costume draped over his back and head, with neat circular cutout holes showing his dark eyes and his brown floppy hound ears poking out through two ear slits.

LOCATION
  The exact same boutique dressing room area with rich dark red velvet curtains in the background and a soft beige carpeted floor.

FIRST FRAME AND BLOCKING
  The red velvet dressing room curtain parts. Charlie steps forward on all four paws into center frame, facing forward.

ACTION & CAMERA
  Eye-level dog camera framing matching the series.
  Charlie steps out from between the red velvet curtains into center frame draped in the white ghost sheet with his ears poking out. He pauses center frame, gives the camera a deadpan, unimpressed stare, gives a gentle head shake, then turns around in an arc with the white sheet flowing softly, and trots deliberately back inside behind the red velvet curtains.

OPTICS / CAMERA
  Low eye-level camera matching dachshund eye height, steady locked-off framing.

PHYSICS
  Natural dachshund walking gait, soft lightweight white cloth flowing over his back and moving with his steps, ears flopping through the cutouts.

LIGHTING
  Warm boutique lighting, soft highlights on the white fabric and his reddish coat.

AUDIO
  Soft fabric rustle of velvet curtains and lightweight sheet, tiny dog paws softly on carpet, a quiet gentle dog sigh. No dialogue, no human speech.
"""
    },
    {
        "id": "scene5_dracula",
        "title": "Scene 5: Spooky Dracula with Cape (The Winner!)",
        "output": str(repo_root / "projects" / "lonestar-doxietalk-halloween" / "assets" / "video" / "scene5_dracula_5s.mp4"),
        "prompt": """GLOBAL STYLE
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
    }
]

def main():
    tool = SeedanceVideo()
    print(f"Starting batch generation of the final {len(jobs)} Charlie costume clips...")

    for i, job in enumerate(jobs, 1):
        print(f"\n=======================================================")
        print(f"[{i}/{len(jobs)}] Launching {job['title']}...")
        print(f"Output: {job['output']}")
        print(f"=======================================================")

        inputs = {
            "prompt": job["prompt"],
            "operation": "reference_to_video",
            "model_version": "2.5",
            "model_variant": "standard",
            "duration": "5",
            "aspect_ratio": "16:9",
            "resolution": "720p",
            "generate_audio": True,
            "reference_image_paths": [ref_charlie],
            "output_path": job["output"],
        }

        start_t = time.time()
        result = tool.execute(inputs)
        elapsed = round(time.time() - start_t, 2)
        print(f"Result success: {result.success} (took {elapsed}s)")

        if not result.success:
            print(f"Error in {job['id']}: {result.error}")
        else:
            print(f"Successfully saved {job['id']} to {job['output']}")

    print("\nBatch generation complete!")

if __name__ == "__main__":
    main()
