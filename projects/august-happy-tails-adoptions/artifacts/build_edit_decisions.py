import json
import os

def build_manifest_and_edits():
    base_dir = os.path.abspath(".")
    proj_dir = os.path.join(base_dir, "projects", "august-happy-tails-adoptions")
    img_dir = os.path.join(proj_dir, "assets", "images")
    audio_path = os.path.join(proj_dir, "assets", "audio", "august_happy_tails_full_eleven_v3.mp3")
    ctdr_logo_path = os.path.join(img_dir, "ctdr.png")
    
    LOGO_SIZE = 520
    TOTAL_DURATION = 322.08

    # 1. Update asset_manifest.json
    manifest = {
        "version": "1.0",
        "assets": [
            {"id": "img-lexie", "type": "image", "path": os.path.join(img_dir, "Lexie Adoption.jpg"), "source_tool": "user_upload", "scene_id": "scene-lexie", "duration_seconds": 25.9},
            {"id": "img-cerberus", "type": "image", "path": os.path.join(img_dir, "Cerberus Adoption.jpg"), "source_tool": "user_upload", "scene_id": "scene-cerberus", "duration_seconds": 33.2},
            {"id": "img-kraken", "type": "image", "path": os.path.join(img_dir, "Kraken Adoption.jpg"), "source_tool": "user_upload", "scene_id": "scene-kraken", "duration_seconds": 32.8},
            {"id": "img-mermaid", "type": "image", "path": os.path.join(img_dir, "Mermaid Adoption.jpg"), "source_tool": "user_upload", "scene_id": "scene-mermaid", "duration_seconds": 24.9},
            {"id": "img-pegasus", "type": "image", "path": os.path.join(img_dir, "Pegasus Adoption.jpeg"), "source_tool": "user_upload", "scene_id": "scene-pegasus", "duration_seconds": 22.9},
            {"id": "img-dallas", "type": "image", "path": os.path.join(img_dir, "Dallas Adoption.jpg"), "source_tool": "user_upload", "scene_id": "scene-dallas", "duration_seconds": 26.1},
            {"id": "img-yeti", "type": "image", "path": os.path.join(img_dir, "Yeti Adoption.jpg"), "source_tool": "user_upload", "scene_id": "scene-yeti", "duration_seconds": 24.8},
            {"id": "img-griffin", "type": "image", "path": os.path.join(img_dir, "Griffin Adoption.jpg"), "source_tool": "user_upload", "scene_id": "scene-griffin", "duration_seconds": 20.9},
            {"id": "img-dawson", "type": "image", "path": os.path.join(img_dir, "Dawson Adoption.jpeg"), "source_tool": "user_upload", "scene_id": "scene-dawson", "duration_seconds": 21.2},
            {"id": "img-papi", "type": "image", "path": os.path.join(img_dir, "Papi Adoption.jpg"), "source_tool": "user_upload", "scene_id": "scene-papi", "duration_seconds": 21.5},
            {"id": "img-darlin", "type": "image", "path": os.path.join(img_dir, "Darlin Adoption.jpg"), "source_tool": "user_upload", "scene_id": "scene-darlin", "duration_seconds": 22.5},
            {"id": "img-ctdr-logo", "type": "image", "path": ctdr_logo_path, "source_tool": "user_upload", "scene_id": "global", "duration_seconds": TOTAL_DURATION},
            {"id": "audio-narration", "type": "narration", "path": audio_path, "source_tool": "elevenlabs_tts", "scene_id": "global", "duration_seconds": TOTAL_DURATION}
        ]
    }
    
    manifest_path = os.path.join(proj_dir, "artifacts", "asset_manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print("Saved asset_manifest.json")

    # 2. Build edit_decisions.json with all 11 dogs
    edit_decisions = {
        "version": "1.0",
        "render_runtime": "remotion",
        "renderer_family": "explainer-data",
        "metadata": {
            "title": "August Happy Tails Adoptions - Full Episode",
            "sample_run": False,
            "dog_count": 11,
            "host": "Charlie",
            "show": "Lone Star Doxie Talk"
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
                "id": "cut-intro",
                "type": "hero_title",
                "source": "img-lexie",
                "logoSrc": ctdr_logo_path,
                "logoSize": LOGO_SIZE,
                "text": "Happy Tails",
                "heroSubtitle": "August Adoptions • Lone Star Doxie Talk",
                "color": "#F59E0B",
                "accentColor": "#F59E0B",
                "in_seconds": 0.0,
                "out_seconds": 19.50,
                "animation": "zoom-in"
            },
            {
                "id": "cut-lexie",
                "type": "image",
                "source": "img-lexie",
                "title": "Lexie",
                "objectFit": "contain",
                "in_seconds": 19.50,
                "out_seconds": 45.40,
                "animation": "ken-burns"
            },
            {
                "id": "cut-cerberus",
                "type": "image",
                "source": "img-cerberus",
                "title": "Cerberus",
                "objectFit": "contain",
                "in_seconds": 45.40,
                "out_seconds": 78.60,
                "animation": "ken-burns"
            },
            {
                "id": "cut-kraken",
                "type": "image",
                "source": "img-kraken",
                "title": "Kraken",
                "objectFit": "contain",
                "in_seconds": 78.60,
                "out_seconds": 111.40,
                "animation": "ken-burns"
            },
            {
                "id": "cut-mermaid",
                "type": "image",
                "source": "img-mermaid",
                "title": "Mermaid",
                "objectFit": "contain",
                "in_seconds": 111.40,
                "out_seconds": 136.30,
                "animation": "ken-burns"
            },
            {
                "id": "cut-pegasus",
                "type": "image",
                "source": "img-pegasus",
                "title": "Pegasus",
                "objectFit": "contain",
                "in_seconds": 136.30,
                "out_seconds": 159.20,
                "animation": "ken-burns"
            },
            {
                "id": "cut-dallas",
                "type": "image",
                "source": "img-dallas",
                "title": "Dallas",
                "objectFit": "contain",
                "in_seconds": 159.20,
                "out_seconds": 185.30,
                "animation": "ken-burns"
            },
            {
                "id": "cut-yeti",
                "type": "image",
                "source": "img-yeti",
                "title": "Yeti",
                "objectFit": "contain",
                "in_seconds": 185.30,
                "out_seconds": 210.10,
                "animation": "ken-burns"
            },
            {
                "id": "cut-griffin",
                "type": "image",
                "source": "img-griffin",
                "title": "Griffin",
                "objectFit": "contain",
                "in_seconds": 210.10,
                "out_seconds": 231.00,
                "animation": "ken-burns"
            },
            {
                "id": "cut-dawson",
                "type": "image",
                "source": "img-dawson",
                "title": "Dawson",
                "objectFit": "contain",
                "in_seconds": 231.00,
                "out_seconds": 252.20,
                "animation": "ken-burns"
            },
            {
                "id": "cut-papi",
                "type": "image",
                "source": "img-papi",
                "title": "Papi",
                "objectFit": "contain",
                "in_seconds": 252.20,
                "out_seconds": 273.70,
                "animation": "ken-burns"
            },
            {
                "id": "cut-darlin",
                "type": "image",
                "source": "img-darlin",
                "title": "Darlin",
                "objectFit": "contain",
                "in_seconds": 273.70,
                "out_seconds": 296.20,
                "animation": "ken-burns"
            },
            {
                "id": "cut-outro",
                "type": "hero_title",
                "source": "img-darlin",
                "logoSrc": ctdr_logo_path,
                "logoSize": LOGO_SIZE,
                "text": "Happy Tails",
                "heroSubtitle": "Thank You Fosters, Adopters & Supporters",
                "color": "#F59E0B",
                "accentColor": "#F59E0B",
                "in_seconds": 296.20,
                "out_seconds": TOTAL_DURATION,
                "animation": "zoom-out"
            }
        ],
        "overlays": [
            {"type": "section_title", "text": "Lexie", "subtitle": "Bruce & Martha • Round Rock, TX", "in_seconds": 19.50, "out_seconds": 44.50, "position": "bottom-left", "accentColor": "#F59E0B"},
            {"type": "section_title", "text": "Cerberus", "subtitle": "Dave & Beth • Round Rock, TX", "in_seconds": 45.40, "out_seconds": 77.60, "position": "bottom-left", "accentColor": "#F59E0B"},
            {"type": "section_title", "text": "Kraken", "subtitle": "Scott • Leander, TX", "in_seconds": 78.60, "out_seconds": 110.40, "position": "bottom-left", "accentColor": "#F59E0B"},
            {"type": "section_title", "text": "Mermaid", "subtitle": "Fostered by Perla • Adopted by Jennifer (Austin, TX)", "in_seconds": 111.40, "out_seconds": 135.30, "position": "bottom-left", "accentColor": "#F59E0B"},
            {"type": "section_title", "text": "Pegasus", "subtitle": "Fostered by Alison • Adopted by Peter & Heather (Hutto, TX)", "in_seconds": 136.30, "out_seconds": 158.20, "position": "bottom-left", "accentColor": "#F59E0B"},
            {"type": "section_title", "text": "Dallas", "subtitle": "Fostered & Adopted by Chad & Tammy (Manchaca, TX)", "in_seconds": 159.20, "out_seconds": 184.30, "position": "bottom-left", "accentColor": "#F59E0B"},
            {"type": "section_title", "text": "Yeti", "subtitle": "Adopted by Tate (Austin, TX)", "in_seconds": 185.30, "out_seconds": 209.10, "position": "bottom-left", "accentColor": "#F59E0B"},
            {"type": "section_title", "text": "Griffin", "subtitle": "Fostered by Alison • Adopted by John & Brianna (Spicewood, TX)", "in_seconds": 210.10, "out_seconds": 230.00, "position": "bottom-left", "accentColor": "#F59E0B"},
            {"type": "section_title", "text": "Dawson", "subtitle": "Fostered by Christine • Adopted by Amber & Michael (Elgin, TX)", "in_seconds": 231.00, "out_seconds": 251.20, "position": "bottom-left", "accentColor": "#F59E0B"},
            {"type": "section_title", "text": "Papi", "subtitle": "Boarded at Day Lily • Adopted by Maggie (Spring, TX)", "in_seconds": 252.20, "out_seconds": 272.70, "position": "bottom-left", "accentColor": "#F59E0B"},
            {"type": "section_title", "text": "Darlin", "subtitle": "Fostered & Adopted by George (Cibolo, TX)", "in_seconds": 273.70, "out_seconds": 295.20, "position": "bottom-left", "accentColor": "#F59E0B"}
        ],
        "captions": []
    }

    edits_path = os.path.join(proj_dir, "artifacts", "edit_decisions.json")
    with open(edits_path, "w", encoding="utf-8") as f:
        json.dump(edit_decisions, f, indent=2)
    print("Saved edit_decisions.json with 11 dogs!")

if __name__ == "__main__":
    build_manifest_and_edits()
