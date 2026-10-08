import json
import os
import jsonschema

proj_dir = os.path.abspath("projects/lonestar_doxietalk_ep12")
art_dir = os.path.join(proj_dir, "artifacts")
os.makedirs(art_dir, exist_ok=True)

# 1. Text description
desc_path = os.path.join(art_dir, "youtube_description.txt")

description_text = """🎃 LONE STAR DOXIE TALK — EPISODE 12: SPOOKY DRACULA CHARLIE & WIENERFEST 2026! 🐾

Pull up a chair and sit a spell, friends! I'm Charlie, and this here's Lone Star Doxie Talk — Episode 12! October has rolled right on in, and you know what that means: crisp autumn air, Halloween preparations, and plenty of doxie excitement across the great state of Texas! 🍁🏡

In today's special episode, we take you behind the scenes down to the costume shop where I try on candidate costumes (from a hot dog to a Texas cowboy, a pumpkin, and a spooky ghost) before crowning this year's winner: Spooky Dracula! 🧛‍♂️

Then, we get down to the business of the heart:
💰 Big Texas-Sized Thanks: Giving gratitude to everyone who donated to our CTDR Summertime Fundraiser to help fund boarding at Day Lily, spay/neuter surgeries, vet care, and heartworm treatments!
📅 2027 CTDR Wall Calendar: Packed full of sweet dachshund faces and perfect for Christmas gifts!
🎪 Wienerfest 2026: Zilkerbark's 4th Annual Wiener Dog meetup is happening Saturday, October 31, 2026, at Sherwood Forest Faire in McDade, Texas!
🎗️ Breast Cancer Awareness Month: Reflecting on the 2026 theme ('Every story is unique, every journey matters') and the life-saving importance of early detection.
🐾 September Happy Tails Adoptions: Celebrating handsome Otis in Lake Jackson and gorgeous Chimera in Round Rock (a wonderful foster failure reunited with her brother Cerberus)!

==================================================
⏱️ CHAPTER TIMESTAMPS
==================================================
0:00 - Introduction & Halloween Excitement
0:44 - The Costume Shop Try-On Montage (Hot Dog, Cowboy, Pumpkin, Ghost)
1:09 - Dracula Charlie Reveal & Spooky Season Kickoff
1:19 - Summertime Fundraiser Thank You (Day Lily, Vet Care, Heartworm)
1:49 - Order Your CTDR 2027 Wall Calendar!
2:06 - Wienerfest 2026 Announcement (Oct 31, McDade, TX)
2:48 - Breast Cancer Awareness Month: Early Detection Saves Lives
3:36 - September Happy Tails Adoptions Showcase
3:45 - Otis Finds His Forever Home (Lake Jackson, TX)
4:12 - Chimera's Foster Failure & Cerberus Reunion (Round Rock, TX)
4:56 - Celebrating Our Fosters, Adopters & Volunteers
5:15 - How to Support CTDR & Charlie's Sign-Off

==================================================
🐾 SUPPORT CENTRAL TEXAS DACHSHUND RESCUE (CTDR)
==================================================
Central Texas Dachshund Rescue is a 501(c)(3) non-profit rescue dedicated to saving, rehabilitating, and rehoming dachshunds in need.

🌐 Official Website: https://www.ctdr.org
💖 Donate to Help Rescue Pups: https://www.ctdr.org [INSERT URL: Direct CTDR Donation Page]
🏡 Adopt a Doxie: https://www.ctdr.org [INSERT URL: CTDR Adoption Application]
🤝 Become a Foster Hero: https://www.ctdr.org [INSERT URL: CTDR Foster Application]
📅 Order the 2027 Wall Calendar: https://www.ctdr.org [INSERT URL: 2027 Wall Calendar Order Link]
🎪 Wienerfest 2026 Tickets: https://www.zilkerbark.com/texas-wienerfest#tickets
🎗️ Breast Cancer Screening Info: [INSERT URL: Healthcare / Screening Resources]

==================================================
"Until next time, remember, a rescued heart never forgets." — Charlie 🐾
==================================================

#Dachshund #CTDR #CentralTexasDachshundRescue #LoneStarDoxieTalk #AdoptDontShop #RescueDogs #WienerDog #DoxieLove #HappyTails #HalloweenDogs #Wienerfest #BreastCancerAwareness
"""

with open(desc_path, "w", encoding="utf-8") as f:
    f.write(description_text.strip() + "\n")
print("Wrote youtube_description.txt to:", desc_path)

# 2. publish_manifest.json
manifest = {
    "version": "1.0",
    "project_id": "lonestar_doxietalk_ep12",
    "title": "Lone Star Doxie Talk - Episode 12: Halloween Special & September Happy Tails",
    "status": "ready_for_publish",
    "platform": "youtube",
    "metadata": {
        "title": "Lone Star Doxie Talk Ep. 12 | Halloween Special: Dracula Charlie, Wienerfest & Happy Tails!",
        "description_file": "artifacts/youtube_description.txt",
        "thumbnail_file": "renders/youtube_thumbnail.png",
        "video_file": "renders/final_episode.mp4",
        "total_duration_seconds": 345.2,
        "tags": [
            "Dachshund",
            "CTDR",
            "Central Texas Dachshund Rescue",
            "Lone Star Doxie Talk",
            "Adopt Dont Shop",
            "Rescue Dogs",
            "Wiener Dog",
            "Happy Tails",
            "Wienerfest 2026",
            "Dracula Charlie",
            "Breast Cancer Awareness"
        ],
        "chapters": [
            {"time": "0:00", "title": "Introduction & Halloween Excitement"},
            {"time": "0:44", "title": "Costume Shop Try-On Montage"},
            {"time": "1:09", "title": "Dracula Charlie Reveal"},
            {"time": "1:19", "title": "Summertime Fundraiser Thank You"},
            {"time": "1:49", "title": "Order Your CTDR 2027 Wall Calendar"},
            {"time": "2:06", "title": "Wienerfest 2026 Announcement (McDade, TX)"},
            {"time": "2:48", "title": "Breast Cancer Awareness Month: Early Detection"},
            {"time": "3:36", "title": "September Happy Tails Adoptions"},
            {"time": "3:45", "title": "Happy Tails: Otis (Lake Jackson, TX)"},
            {"time": "4:12", "title": "Happy Tails: Chimera & Cerberus (Round Rock, TX)"},
            {"time": "4:56", "title": "Thank You Fosters & Adopters"},
            {"time": "5:15", "title": "How to Support CTDR & Sign-Off"}
        ]
    }
}

manifest_path = os.path.join(art_dir, "publish_manifest.json")
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2)
print("Wrote publish_manifest.json to:", manifest_path)

# 3. publish_log.json
schema_path = os.path.abspath("schemas/artifacts/publish_log.schema.json")
with open(schema_path, "r", encoding="utf-8") as sf:
    schema = json.load(sf)

publish_log = {
    "version": "1.0",
    "entries": [
        {
            "platform": "youtube",
            "status": "pending_review",
            "export_path": "renders/youtube_thumbnail.png",
            "timestamp": "2026-10-08T09:25:00Z",
            "metadata_used": {
                "title": manifest["metadata"]["title"],
                "description": description_text.strip(),
                "hashtags": manifest["metadata"]["tags"],
                "chapters": manifest["metadata"]["chapters"]
            }
        }
    ],
    "metadata": {
        "project_id": "lonestar_doxietalk_ep12",
        "thumbnail_path": "renders/youtube_thumbnail.png",
        "description_path": "artifacts/youtube_description.txt"
    }
}

jsonschema.validate(instance=publish_log, schema=schema)
print("publish_log.json schema validation: PASSED!")

log_path = os.path.join(art_dir, "publish_log.json")
with open(log_path, "w", encoding="utf-8") as f:
    json.dump(publish_log, f, indent=2)
print("Wrote publish_log.json to:", log_path)
