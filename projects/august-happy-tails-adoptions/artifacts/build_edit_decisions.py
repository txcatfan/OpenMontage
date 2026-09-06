import json
import os

def build_edit_decisions():
    base_dir = os.path.abspath(".")
    proj_dir = os.path.join(base_dir, "projects", "august-happy-tails-adoptions")
    
    audio_path = os.path.join(proj_dir, "assets", "audio", "august_happy_tails_sample_v4_eleven_v3.mp3")
    ctdr_logo_path = os.path.join(proj_dir, "assets", "images", "ctdr.png")
    
    # 2x logo size from Test #3: 260 * 2 = 520px
    LOGO_SIZE = 520
    
    # Exact cues aligned with Eleven v3 audio (147.28s total duration)
    # Intro: 0.0 - 19.14s
    # Lexie: 19.14 - 44.39s
    # Cerberus: 44.39 - 75.80s
    # Kraken: 75.80 - 108.36s
    # Mermaid: 108.36 - 135.02s
    # Outro: 135.02 - 147.28s

    edit_decisions = {
        "version": "1.0",
        "render_runtime": "remotion",
        "renderer_family": "explainer-data",
        "metadata": {
            "title": "August Happy Tails Adoptions - Test Video #4",
            "sample_run": True,
            "dog_count": 4,
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
                "out_seconds": 19.14,
                "animation": "zoom-in"
            },
            {
                "id": "cut-lexie",
                "type": "image",
                "source": "img-lexie",
                "title": "Lexie",
                "objectFit": "contain",
                "in_seconds": 19.14,
                "out_seconds": 44.39,
                "animation": "ken-burns"
            },
            {
                "id": "cut-cerberus",
                "type": "image",
                "source": "img-cerberus",
                "title": "Cerberus",
                "objectFit": "contain",
                "in_seconds": 44.39,
                "out_seconds": 75.80,
                "animation": "ken-burns"
            },
            {
                "id": "cut-kraken",
                "type": "image",
                "source": "img-kraken",
                "title": "Kraken",
                "objectFit": "contain",
                "in_seconds": 75.80,
                "out_seconds": 108.36,
                "animation": "ken-burns"
            },
            {
                "id": "cut-mermaid",
                "type": "image",
                "source": "img-mermaid",
                "title": "Mermaid",
                "objectFit": "contain",
                "in_seconds": 108.36,
                "out_seconds": 135.02,
                "animation": "ken-burns"
            },
            {
                "id": "cut-outro",
                "type": "hero_title",
                "source": "img-mermaid",
                "logoSrc": ctdr_logo_path,
                "logoSize": LOGO_SIZE,
                "text": "Happy Tails",
                "heroSubtitle": "Thank You Fosters, Adopters & Supporters",
                "color": "#F59E0B",
                "accentColor": "#F59E0B",
                "in_seconds": 135.02,
                "out_seconds": 147.28,
                "animation": "zoom-out"
            }
        ],
        "overlays": [
            {
                "type": "section_title",
                "text": "Lexie",
                "subtitle": "Bruce & Martha • Round Rock, TX",
                "in_seconds": 19.14,
                "out_seconds": 43.5,
                "position": "bottom-left",
                "accentColor": "#F59E0B"
            },
            {
                "type": "section_title",
                "text": "Cerberus",
                "subtitle": "Dave & Beth • Round Rock, TX",
                "in_seconds": 44.39,
                "out_seconds": 74.8,
                "position": "bottom-left",
                "accentColor": "#F59E0B"
            },
            {
                "type": "section_title",
                "text": "Kraken",
                "subtitle": "Scott • Leander, TX",
                "in_seconds": 75.80,
                "out_seconds": 107.4,
                "position": "bottom-left",
                "accentColor": "#F59E0B"
            },
            {
                "type": "section_title",
                "text": "Mermaid",
                "subtitle": "Fostered by Perla • Adopted by Jennifer (Austin, TX)",
                "in_seconds": 108.36,
                "out_seconds": 134.0,
                "position": "bottom-left",
                "accentColor": "#F59E0B"
            }
        ],
        "captions": []
    }
    
    out_file = os.path.join(proj_dir, "artifacts", "edit_decisions.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(edit_decisions, f, indent=2)
    print("Updated edit_decisions.json at:", out_file)

if __name__ == "__main__":
    build_edit_decisions()
