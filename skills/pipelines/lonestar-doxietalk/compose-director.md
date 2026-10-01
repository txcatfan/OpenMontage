# Compose Director - Lone Star Doxie Talk Pipeline

## When To Use
Use at Stage 6 (`compose`) to execute the final master video render.

## Render Flow
1. **Render Sub-Compositions:** Render any Remotion motion-graphics scenes (e.g. Happy Tails showcase) to intermediate MP4.
2. **Execute Master Stitch:** Using OpenMontage `video_stitch` or FFmpeg, concatenate the sequence according to `edit_decisions.json`.
3. **Verify Master Output:**
   - Confirm video exists at `renders/final_episode.mp4`.
   - Confirm resolution is 1080p or 720p 16:9 widescreen.
   - Confirm audio stream is present, synchronized, and free of clipping.
4. **Produce Artifact:** Schema-valid `render_report.json`.
