# Publish Director - Lone Star Doxie Talk Pipeline

## When To Use
Use at Stage 7 (`publish`) to generate the complete YouTube packaging kit.

## Responsibilities
1. **Analyze Full Episode Dialogue:** Read all section scripts from Stage 2.
2. **Generate YouTube Description:**
   * Warm opening in Charlie's voice with emoji highlights (🏡, 🐾, 💰).
   * Exact chapter timestamps for each segment (e.g. `0:00 Introduction`, `0:45 Happy Tails Adoptions`, etc.).
   * CTDR links: official site (`https://www.ctdr.org`), donation links, foster applications.
   * Format any missing links with explicit placeholders: `[INSERT URL: brief description]`.
   * Standard sign-off: `"Until next time, remember, a rescued heart never forgets." — Charlie 🐾`.
   * 5–10 relevant hashtags: `#Dachshund #CTDR #AdoptDontShop #LoneStarDoxieTalk #RescueDogs`.
3. **Format YouTube Thumbnail:** Ensure a 1280x720 (16:9) thumbnail image is exported to `renders/youtube_thumbnail.png`.
4. **Produce Artifact:** Schema-valid `publish_manifest.json`.

## Gate Reminder
Gated on human approval (`human_approval_default: true`). Checkpoint as `awaiting_human`, present the YouTube description and thumbnail for user review, and conclude the episode pipeline.
