# Scene Director - Lone Star Doxie Talk Pipeline

## When To Use
Use at Stage 3 (`scene_plan`) to map the visual storyboard, segment timings, card transitions, and audio ducking.

## Scene Architecture
1. **Scene 1: Host Monologue Plate:** Charlie on-camera at studio desk. Lower-third: episode title & CTDR badge.
2. **Scene 2: Happy Tails Montage:** Remotion motion graphics reel. Each dog receives an animated card with photo, name, adoption month, and CTDR watermark.
3. **Scene 3: Optional Cutaway / Sketch / Memorial:** Transition to custom video (e.g. Charlie in dressing room) or solemn memorial photo sequence.
4. **Scene 4: Episode Conclusion Plate:** Return to Charlie at studio desk for recap and call-to-action.
5. **Scene 5: Outro Card:** Full-screen CTDR website (`ctdr.org`), donation QR code, and social links.

## Audio & Music Planning
* **Music Stem:** Warm acoustic guitar track from library.
* **Ducking:** -18dB under speech with 0.5s fade ramps. Full volume on segment transitions.

## Gate Reminder
Gated on human approval (`human_approval_default: true`). Checkpoint as `awaiting_human`, present scene layout, and pause for approval.
