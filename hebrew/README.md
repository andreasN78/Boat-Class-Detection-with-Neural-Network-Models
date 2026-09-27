# Ivrit Daily: spoken Hebrew in 30 days

A daily program for learning **spoken** Israeli Hebrew, made for a native Greek speaker who also speaks English.
There is no Hebrew writing to learn: every word is spelled the way it sounds, with the **stressed syllable in CAPS**.

| File | What it is |
|---|---|
| `index.html` | The app. Open it in any browser. 30 days, ▶ audio (uses your device's Hebrew voice), practice mode, progress tracking. |
| `hebrew-daily.ics` | Calendar file: one event per day at 09:00 starting **Mon 28 Sep 2026**, with that day's words and an alarm. Import it on your phone to get daily notifications. |
| `lessons.json` | All lesson content (26 lessons, 210 words and phrases, Greek + English meanings). |
| `build.py` | Rebuilds `index.html` and the `.ics` from `lessons.json`. Change `START` to move day 1. |

## The plan

- 6 lesson days, then 1 review day (days 7, 14, 21, 28), 26 lessons in total.
- Week 1: greetings, basics, introducing yourself, numbers, questions, survival phrases.
- Week 2: family, food, café, everyday verbs, time, days of the week.
- Week 3: directions, places, adjectives, feelings, slang, numbers and money.
- Week 4: shopping, health, past tense, future tense, weather, daily routine.
- Days 29–30: linking words, wishes and celebrations.

Each day takes about 15 minutes: listen and repeat, say the sentence of the day three times,
then switch on Practice (Greek visible, Hebrew blurred) and test yourself out loud.

## Reading the pronunciation

- **kh** = Greek χ (χαρά). **r** = throaty, like French r / Greek γ in γάλα, never rolled.
- **ts** = τσ. **sh** = English "sh". **h** = light breath.
- Vowels ah, eh, ee, oh, oo = Greek α, ε, ι, ο, ου.
- **a / b** pairs: first form for a man, second for a woman.

## Getting the calendar reminders

1. Open `hebrew/hebrew-daily.ics` on GitHub and download it (Raw → save).
2. iPhone: open the file → *Add All*. Android: open it with Google Calendar (or import it at calendar.google.com → Settings → Import).
3. The events use your phone's local time, so 09:00 is 09:00 wherever you are.
