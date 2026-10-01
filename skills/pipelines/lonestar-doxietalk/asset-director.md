# Asset Director - Lone Star Doxie Talk Pipeline

## When To Use
Use at Stage 4 (`assets`) to synthesize voiceovers, render host avatar video, and format dog adoption photography.

## Asset Generation Workflows

### 1. Narration Audio (TTS)
* **Provider:** ElevenLabs (`elevenlabs_tts`)
* **Voice ID:** `CHARLIE_VOICE_ID=GdPqjbdsuwHYqzHrC45c`
* **Output Tracks:**
  - `assets/audio/monologue_audio.mp3`
  - `assets/audio/happy_tails_audio.mp3`
  - `assets/audio/conclusion_audio.mp3`

### 2. Host Avatar Video
* **Provider:** Kling AI Avatar (`kling_official_video`) or Seedance 2.5 (`seedance_video`)
* **Base Image:** `charlie_podcast_host_16x9.png` (or seasonal variant)
* **Outputs:**
  - `assets/video/host_intro.mp4`
  - `assets/video/host_conclusion.mp4`

### 3. Happy Tails Dog Photography
* **Ingest:** Collect dog photos into `assets/images/happy_tails/`.
* **Framing:** Center subjects, crop to 16:9 card aspect or composite with blurred backdrops for vertical photos.

### 4. Background Music
* Check `music_library/` for warm acoustic folk/country guitar tracks.

## Gate Reminder
Gated on human approval (`human_approval_default: true`). Checkpoint as `awaiting_human`, present assets list and audio samples, and pause for approval.
