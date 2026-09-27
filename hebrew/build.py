"""Build the Ivrit Daily app and calendar reminders from lessons.json.

Outputs:
  index.html         standalone page (open in any browser)
  hebrew-daily.ics   30 daily calendar events with the day's words and a reminder alarm
"""
import json
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).parent
START = date(2026, 9, 28)  # Day 1
REMINDER_TIME = "090000"   # local time, floating (follows the phone's time zone)
REVIEW_DAYS = {7, 14, 21, 28}

lessons = json.loads((HERE / "lessons.json").read_text(encoding="utf-8"))


def schedule():
    days, li, week = [], 0, []
    for d in range(1, 31):
        if d in REVIEW_DAYS:
            days.append((d, None, week))
            week = []
        else:
            days.append((d, li, None))
            week.append(li)
            li += 1
    return days


def ics_escape(text):
    return text.replace("\\", "\\\\").replace(";", "\;").replace(",", "\\,").replace("\n", "\\n")


def fold(line):
    """Fold to 75 octets per RFC 5545 without splitting UTF-8 characters."""
    out, cur = [], ""
    for ch in line:
        limit = 75 if not out else 74
        if len((cur + ch).encode("utf-8")) > limit:
            out.append(cur)
            cur = ch
        else:
            cur += ch
    out.append(cur)
    return "\r\n ".join(out)


def build_ics():
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Ivrit Daily//EN",
             "CALSCALE:GREGORIAN", "X-WR-CALNAME:Ivrit Daily (Hebrew)"]
    for d, li, week in schedule():
        day = START + timedelta(days=d - 1)
        if li is not None:
            L = lessons[li]
            summary = f"Hebrew day {d}: {L['title']} / {L['el_title']}"
            body = [f"{w['s']}  =  {w['el']}  /  {w['en']}" for w in L["words"]]
            body += ["", "Sentence: " + L["sentence"]["s"], "= " + L["sentence"]["el"]]
            if L.get("tip"):
                body += ["", "Tip: " + L["tip"]]
        else:
            summary = f"Hebrew day {d}: review of the week / Επανάληψη"
            body = ["Say each one out loud from the Greek:"]
            body += [f"{w['el']}  →  {w['s']}" for i in week for w in lessons[i]["words"]]
        desc = "\n".join(body) + "\n\n(CAPS = stressed syllable, kh = Greek χ)"
        stamp = day.strftime("%Y%m%d")
        lines += [
            "BEGIN:VEVENT",
            f"UID:ivrit-daily-{d}@hebrew-course",
            "DTSTAMP:20260927T000000Z",
            f"DTSTART:{stamp}T{REMINDER_TIME}",
            "DURATION:PT15M",
            fold("SUMMARY:" + ics_escape(summary)),
            fold("DESCRIPTION:" + ics_escape(desc)),
            "BEGIN:VALARM", "ACTION:DISPLAY", fold("DESCRIPTION:" + ics_escape(summary)),
            "TRIGGER:PT0M", "END:VALARM",
            "END:VEVENT",
        ]
    lines.append("END:VCALENDAR")
    (HERE / "hebrew-daily.ics").write_text("\r\n".join(lines) + "\r\n", encoding="utf-8")


def build_html():
    page = (HERE / "template.html").read_text(encoding="utf-8")
    page = page.replace("__LESSONS__", json.dumps(lessons, ensure_ascii=False)).replace("__START__", START.isoformat())
    head, _, rest = page.partition("<style>")
    full = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            + head + "<style>" + rest.replace("</style>", "</style>\n</head>\n<body>", 1) + "\n</body>\n</html>\n")
    (HERE / "index.html").write_text(full, encoding="utf-8")


if __name__ == "__main__":
    build_ics()
    build_html()
    print("Built index.html and hebrew-daily.ics")
