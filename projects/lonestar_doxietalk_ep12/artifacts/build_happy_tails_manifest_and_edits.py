import json
import os

def build():
    base_dir = os.path.abspath(".")
    proj_dir = os.path.join(base_dir, "projects", "lonestar_doxietalk_ep12")
    img_dir = os.path.join(proj_dir, "assets", "images", "september_adoptions")
    audio_path = os.path.join(proj_dir, "assets", "audio", "scene4_happy_tails_audio.mp3")
    ctdr_logo_path = os.path.join(proj_dir, "assets", "images", "ctdr.png")

    otis_path = os.path.join(img_dir, "Otis Adoption.jpeg")
    chimera_path = os.path.join(img_dir, "Chimera adoption.jpg")
    both_path = os.path.join(img_dir, "both_september_adoptions.png")

    TOTAL_DURATION = 98.08

    # 1. asset_manifest.json
    manifest = {
        "version": "1.0",
        "assets": [
            {
                "id": "img-otis",
                "type": "image",
                "path": otis_path,
                "source_tool": "user_upload",
                "scene_id": "scene-04-happy-tails",
                "duration_seconds": 36.0
            },
            {
                "id": "img-chimera",
                "type": "image",
                "path": chimera_path,
                "source_tool": "user_upload",
                "scene_id": "scene-04-happy-tails",
                "duration_seconds": 44.0
            },
            {
                "id": "img-both-dogs",
                "type": "image",
                "path": both_path,
                "source_tool": "composite",
                "scene_id": "scene-04-happy-tails",
                "duration_seconds": 18.08
            },
            {
                "id": "img-ctdr-logo",
                "type": "image",
                "path": ctddr_logo if 'ctddr_logo' in locals() else ctdr_logo_path,
                "source_tool": "brand_asset",
                "scene_id": "scene-04-happy-tails",
                "duration_seconds": TOTAL_DURATION
            },
            {
                "id": "audio-narration",
                "type": "narration",
                "path": audio_path,
                "source_tool": "elevenlabs_tts",
                "scene_id": "scene-04-happy-tails",
                "duration_seconds": TOTAL_DURATION
            }
        ]
    }

    manifest_path = os.path.join(proj_dir, "artifacts", "asset_manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print("Saved asset_manifest.json to:", manifest_path)

    # 2. edit_decisions.json
    edit_decisions = {
        "version": "1.0",
        "render_runtime": "remotion",
        "renderer_family": "explainer-data",
        "metadata": {
            "title": "September Happy Tails Adoptions - Lone Star Doxie Talk Ep 12",
            "sample_run": False,
            "dog_count": 2,
            "host": "Charlie",
            "show": "Lone Star Doxie Talk",
            "total_duration": TOTAL_DURATION
        },
        "themeConfig": {
            "primaryColor": "#D97706",
            "accentColor": "#F59E0B",
            "backgroundColor": "#0B1120",
            "surfaceColor": "#1E293B",
            "textColor": "#FFFFFF",
            "mutedTextColor": "#CBD5E1",
            "headingFont": "Space Grotesk",
            "bodyFont": "Space Grotesk",
            "monoFont": "Fira Code",
            "chartColors": ["#F59E0B", "#D97706", "#10B981", "#3B82F6"],
            "springConfig": {"damping": 15, "stiffness": 90, "mass": 1},
            "transitionDuration": 0.5,
            "captionHighlightColor": "#F59E0B",
            "captionBackgroundColor": "rgba(11, 17, 32, 0.85)"
        },
        "audio": {
            "narration": {
                "src": audio_path,
                "source": audio_path,
                "volume": 1.0
            }
        },
        "cuts": [
            {
                "id": "cut-otis",
                "type": "image",
                "source": "img-otis",
                "title": "Otis",
                "objectFit": "contain",
                "in_seconds": 0.0,
                "out_seconds": 36.0,
                "animation": "ken-burns"
            },
            {
                "id": "cut-chimera",
                "type": "image",
                "source": "img-chimera",
                "title": "Chimera",
                "objectFit": "contain",
                "in_seconds": 36.0,
                "out_seconds": 80.0,
                "animation": "ken-burns"
            },
            {
                "id": "cut-both-dogs",
                "type": "image",
                "source": "img-both-dogs",
                "title": "Two Precious Lives",
                "objectFit": "contain",
                "in_seconds": 80.0,
                "out_seconds": TOTAL_DURATION,
                "animation": "zoom-in"
            }
        ],
        "overlays": [
            {
                "type": "section_title",
                "text": "Otis",
                "subtitle": "Fostered by Christine • Adopted by Tom & Lana (Lake Jackson, TX)",
                "in_seconds": 0.5,
                "out_seconds": 35.0,
                "position": "bottom-left",
                "accentColor": "#F59E0B"
            },
            {
                "type": "section_title",
                "text": "Chimera",
                "subtitle": "Fostered & Adopted by Dave & Beth (Round Rock, TX)",
                "in_seconds": 36.5,
                "out_seconds": 79.0,
                "position": "bottom-left",
                "accentColor": "#F59E0B"
            },
            {
                "type": "section_title",
                "text": "Happy Tails!",
                "subtitle": "Thank You Fosters, Adopters & CTDR Supporters",
                "in_seconds": 80.5,
                "out_seconds": 97.5,
                "position": "bottom-left",
                "accentColor": "#F59E0B"
            }
        ],
        "captions": []
    }

    edits_path = os.path.join(proj_dir, "artifacts", "edit_decisions.json")
    with open(edits_path, "w", encoding="utf-8") as f:
        json.dump(edit_decisions, f, indent=2)
    print("Saved edit_decisions.json to:", edits_path)

if __name__ == "__main__":
    build()
