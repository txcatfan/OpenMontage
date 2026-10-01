# Lone Star Doxie Talk — Halloween Costume Montage: Test Run Review

## Executive Summary
Two initial 5-second test clips were generated using **ByteDance Seedance 2.5** via `seedance_video` in multimodal `reference_to_video` mode, conditioned directly on Charlie's 8-view turnaround sheet (`charlie_reference_picture.jpg`).

Both clips followed the exact requested comedic beat:
1. Entrance on all fours from behind dark red velvet dressing room curtains.
2. Center-frame stop, eye-contact with the camera, and an unamused / deadpan expression.
3. Turn around and purposeful trot back through the curtain opening to change.

---

## Rendered Video Assets
1. **Scene 1: Classic Hot Dog Costume (v2 Multi-Reference, 5.06s, 720p)**  
   - File: `projects/lonestar-doxietalk-halloween/assets/video/test_hotdog_v2_5s.mp4`
   - Highlights: Fixed rear bun hallucination, two clean side buns, deadpan waddle back through curtain.

2. **Scene 2: Texas Lone Star Cowboy Costume (5.06s, 720p)**  
   - File: `projects/lonestar-doxietalk-halloween/assets/video/test_cowboy_5s.mp4`
   - Highlights: Miniature ten-gallon hat, red paisley bandana, skeptical deadpan stare.

3. **Scene 3: Jack-O'-Lantern Pumpkin Suit (5.06s, 720p)**  
   - File: `projects/lonestar-doxietalk-halloween/assets/video/scene3_pumpkin_5s.mp4`
   - Highlights: Round plush pumpkin suit, green collar, eyes squeezed shut in resignation.

4. **Scene 4: Bed-Sheet Ghost Costume (5.06s, 720p)**  
   - File: `projects/lonestar-doxietalk-halloween/assets/video/scene4_ghost_5s.mp4`
   - Highlights: White ghost sheet with ear slits and eye cutouts, deadpan head shake.

5. **Scene 5 (The Winner): Spooky Dracula with Cape & Fangs (Final, 5.06s, 720p)**  
   - File: `projects/lonestar-doxietalk-halloween/assets/video/scene5_dracula_final_5s.mp4`
   - Highlights: Exact Charlie likeness (solid reddish-tan coat, silver muzzle hairs, dark eyes), high-collared red-lined black satin cape, red bowtie, vest, delicate white canine fangs peeking over lower lip, big happy proud smile, and excited tail wag!

---

## Storyboard Plan for Remaining Clips

| Scene # | Costume | Charlie's Reaction | Action & Pacing |
|---|---|---|---|
| **Scene 1** | Classic Hot Dog | Unimpressed, deadpan sigh | Enters, pauses, turns & exits (Completed) |
| **Scene 2** | Texas Cowboy | Skeptical side-eye | Enters, pauses, turns & exits (Completed) |
| **Scene 3** | Bed-Sheet Ghost / Lion Mane | Annoyed / confused | Enters, shakes head, turns & exits (~5s) |
| **Scene 4** | Spooky Dracula with Cape | **Delighted & Proud!** | Enters, chest out, happy tail wag, stays center stage admiring himself (~5s) |
| **Scene 5 (Transition)** | Studio Hand-off | On-air & ready to record | Cut back to podcast studio with Dracula cape on |

---

## Seedance 2.5 vs. Kling v3 Comparison

| Metric / Dimension | ByteDance Seedance 2.5 (`seedance_video`) | Kling v3 Standard (`kling_video`) |
|---|---|---|
| **Input Type** | Direct multimodal reference (`reference_to_video` using turnaround sheet) | Image-to-Video (`image_to_video` from starting costume frame) |
| **Cost per 5s Clip** | ~$1.50 | ~$0.10 (15× cheaper) |
| **Generation Time** | ~180 – 270s | ~55 – 65s |
| **Spatial / Staging Control** | Exceptional: walked out from curtain, turned around, and waddled straight back through the center opening in both clips. | Very Good: fluid turn and exit. Hot dog clip exited through the curtain; cowboy clip turned and walked off-screen right. |
| **Character Likeness** | Exact match to Charlie's 8-view turnaround sheet (face, coat, silver snout, dark eyes). | Preserved starting frame likeness accurately throughout the animation. |
| **Native Audio** | Yes (subtle curtain fabric rustles, gentle paw clicks, quiet sigh). | Audio stream present, but primarily ambient silence. |

### Generated Files Summary
* **Seedance Hot Dog:** `projects/lonestar-doxietalk-halloween/assets/video/test_hotdog_5s.mp4`
* **Seedance Cowboy:** `projects/lonestar-doxietalk-halloween/assets/video/test_cowboy_5s.mp4`
* **Kling Hot Dog:** `projects/lonestar-doxietalk-halloween/assets/video/kling_test_hotdog_5s.mp4`
* **Kling Cowboy:** `projects/lonestar-doxietalk-halloween/assets/video/kling_test_cowboy_5s.mp4`

