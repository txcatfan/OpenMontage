# Script Director - Lone Star Doxie Talk Pipeline

## When To Use
Use at Stage 2 (`script`) to write Charlie's spoken dialogue for all segments of the episode.

## Core Rules for Charlie's Voice

### Mandatory Anchor Lines:
1. **Episode Monologue Opening:** Default opening (can be overridden for special editions):
   > *"Pull up a chair and sit a spell.   I'm Charlie and this here's Lone Star Doxie Talk."*
2. **Episode Conclusion Sign-Off:** Must end exactly with:
   > *"Until next time, remember, a rescued heart never forgets."*

### Critical Formatting for ElevenLabs TTS:
* **Double-Newline Paragraph Breaks:** Every section, distinct topic, and individual dog story MUST be separated by double newlines (`\n\n`). Do NOT output monolithic blocks of text.

### Segment Structure:
1. **Section 1: Host Monologue & CTDR News:** Greeting -> Episode theme -> Community news.
2. **Section 2: Happy Tails Segment:** Dive directly into the dog adoption stories. DO NOT repeat the show greeting or sign-off.
3. **Section 3: Optional Memorial or Sketch:** Respectful Rainbow Bridge tribute or lively comedy cutaway.
4. **Section 4: Conclusion Dialog:** Recap topics covered -> CTDR volunteer/donation call-to-action (`ctdr.org`) -> Mandatory sign-off.

## Few-Shot Style References
When prompting the LLM to draft Charlie's dialogue, always provide few-shot excerpts from the official reference episodes in `assets/lonestar-doxietalk/style_references/`:
* **Happy Tails Style:** `assets/lonestar-doxietalk/style_references/happy_tails/lonestar_doxietalk_ep10_happy_tails_dialog.md`
* **Main Monologue Style:** `assets/lonestar-doxietalk/style_references/main_dialog/lonestar_doxietalk_ep10_dialog.md`

## Gate Reminder
Gated on human approval (`human_approval_default: true`). Checkpoint as `awaiting_human`, present script drafts for user review, and pause for approval.
