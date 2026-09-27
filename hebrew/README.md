# Ivrit Daily: spoken Hebrew in 30 days

A daily program for learning **spoken** Israeli Hebrew, made for a native Greek speaker who also speaks English.
There is no Hebrew writing to learn: every word is spelled the way it sounds, with the **stressed syllable in CAPS**,
and every meaning is given in Greek and English.

Open `index.html` in any browser (phone or computer). Progress is saved in that browser.

## What's in the app

| Tab | What it does |
|---|---|
| **Today** | The day's lesson: 8–10 words and phrases, a sentence of the day and a tip. ▶ plays each one with your device's Hebrew voice. *Practice* hides the Hebrew so you can test yourself; *Mark day done* sends the words to your reviews. |
| **Review** | Spaced repetition. Each word comes back after 1, 3, 7, 14, 30 and 60 days while you know it, and the next day when you don't. See the Greek, say the Hebrew out loud, then check. |
| **Listen & quiz** | *Listen & repeat*: hands-free drill that says each phrase, pauses for you to repeat, and says it again. *Quiz*: hear Hebrew and pick the meaning, or see the meaning and pick the Hebrew. |
| **Phrasebook** | Every word and phrase in one searchable list (search in Greek, English or Hebrew sounds). |
| **Guide & settings** | How to read the pronunciation, the daily routine, and settings: *I speak as a man / a woman* (Hebrew changes some words for men and women), voice speed, start date. |

A bonus lesson (★ at the end of the day strip) collects everyday Hebrew words that come from Greek.

## The plan

- 6 lesson days, then 1 review day (days 7, 14, 21, 28), 26 lessons in total.
- Week 1: greetings, basics, introducing yourself, numbers, questions, survival phrases.
- Week 2: family, food, café, everyday verbs, time, days of the week.
- Week 3: directions, places, adjectives, feelings, slang, numbers and money.
- Week 4: shopping, health, past tense, future tense, weather, daily routine.
- Days 29–30: linking words, wishes and celebrations.

About 15 minutes a day: do your reviews, learn the new lesson out loud, run Listen & repeat once, then mark the day done.

## Reading the pronunciation

- **kh** = Greek χ (χαρά). **r** = throaty, like French r / Greek γ in γάλα, never rolled.
- **ts** = τσ. **sh** = English "sh". **h** = light breath.
- Vowels ah, eh, ee, oh, oo = Greek α, ε, ι, ο, ου.
- Where a phrase has a men's and a women's form, the app shows the one you picked in settings.

## Daily reminders

`hebrew-daily.ics` holds one calendar event per day at 09:00, starting **Mon 28 Sep 2026**, with that day's words and an alarm.

1. Open `hebrew/hebrew-daily.ics` on GitHub and download it (Raw → save).
2. iPhone: open the file → *Add All*. Android: open it with Google Calendar (or import it at calendar.google.com → Settings → Import).
3. The events use your phone's local time, so 09:00 is 09:00 wherever you are.

## Files

| File | What it is |
|---|---|
| `index.html` | The app (built, self-contained). |
| `lessons.json` | The 26 lessons. Each item has `s` (pronunciation), `t` (casual Latin spelling), `he` (Hebrew spelling, used only for the voice), `en`, `el`, and for phrases that differ for men and women `g` plus the women's form in `s_f`, `t_f`, `he_f`. |
| `bonus.json` | The bonus lesson of Hebrew words from Greek. |
| `template.html` | The app's source. |
| `build.py` | Rebuilds `index.html` and `hebrew-daily.ics` from the JSON files (`python3 build.py`). Change `START` to move day 1. |
