"""
Auswertung der strukturierten Logs aus Challenge 3.
Logs aus Coolify (Tab "Logs") kopieren, in logs.txt speichern, dann:
    python3 analyze_logs.py logs.txt
Zeilen ohne JSON (z.B. Gunicorn-Meldungen) werden ignoriert.
"""
import json
import sys
from collections import Counter

path = sys.argv[1] if len(sys.argv) > 1 else "logs.txt"
events = []
with open(path, encoding="utf-8") as f:
    for line in f:
        start = line.find("{")
        if start == -1:
            continue
        try:
            events.append(json.loads(line[start:]))
        except json.JSONDecodeError:
            continue

by_type = Counter(e.get("event") for e in events)
received = [e for e in events if e.get("event") == "request_received"]
success = [e for e in events if e.get("event") == "request_success"]
errors = [e for e in events if e.get("event") == "request_error"]
finished = success + errors
durations = [e["duration_ms"] for e in finished if "duration_ms" in e]
success_durations = [e["duration_ms"] for e in success if "duration_ms" in e]

print(f"Log-Einträge (JSON):        {len(events)}")
print(f"Requests empfangen:         {len(received)}")
print(f"Erfolgreich / fehlerhaft:   {len(success)} / {len(errors)}")
if finished:
    print(f"Erfolgsquote:               {len(success) / len(finished):.0%}")
if durations:
    print(f"Ø Dauer (alle):             {sum(durations) / len(durations):.1f} ms")
if success_durations:
    print(f"Ø Dauer (nur erfolgreich):  {sum(success_durations) / len(success_durations):.1f} ms")
print("\nHäufigste Fehler:")
for err, n in Counter(e.get("error") for e in errors).most_common():
    print(f"  {n}x  {err}")
print("\nEvents nach Typ:")
for ev, n in by_type.most_common():
    print(f"  {n}x  {ev}")
