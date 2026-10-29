#!/usr/bin/env python3
"""Genera data.json: llegeix els calendaris .ics dels equips (camp "ics") i
els combina amb els equips amb partits manuals. Només necessita Python 3.9+."""
import json, re, glob, urllib.request, datetime as dt
from zoneinfo import ZoneInfo

ACR = {"AE", "FS", "CF", "CFS", "UBAE", "CEM", "IES", "UB", "JJ", "CE", "CES", "CCR", "CET", "FCF", "UE", "CD"}
LOW = {"de", "del", "d", "l"}
FIX = {"Gavá": "Gavà", "Cornella": "Cornellà", "Santo Angel": "Santo Ángel"}
MAD = ZoneInfo("Europe/Madrid")


def pretty(s):
    s = re.sub(r"\s*\(.*$", "", re.sub(r"\s+", " ", s)).strip()

    def f(m):
        w = m.group(0)
        if len(w) == 1 or w.upper() in ACR:
            return w.upper()
        return w.lower() if w.lower() in LOW else w.capitalize()

    s = re.sub(r"[\wÀ-ÿ·.]+", f, s)
    for a, b in FIX.items():
        s = s.replace(a, b)
    return s


def parse(text, me):
    text = re.sub(r"\r?\n[ \t]", "", text)
    out = []
    for ev in text.split("BEGIN:VEVENT")[1:]:
        def g(k):
            m = re.search(r"^" + k + r"[^:\r\n]*:(.*)$", ev, re.M)
            return m.group(1).strip().replace("\\,", ",") if m else ""
        mm = re.match(r"(\d{4})(\d\d)(\d\d)T(\d\d)(\d\d)", g("DTSTART"))
        if not mm:
            continue
        when = dt.datetime(*map(int, mm.groups()))
        if g("DTSTART").endswith("Z"):
            when = when.replace(tzinfo=dt.timezone.utc).astimezone(MAD)
        s = re.sub(r"\s+", " ", g("SUMMARY").replace("⚽", "")).strip()
        s = re.sub(r"^FINAL\s*·\s*", "", s)
        sc = re.match(r"^(.+?) (\d+) - (\d+) (.+)$", s)
        if sc:
            home, away, hg, ag = sc[1], sc[4], int(sc[2]), int(sc[3])
        elif " - " in s:
            home, away = s.split(" - ", 1)
            hg = ag = None
        else:
            continue
        is_home = home.upper().startswith(me.upper())
        m = {"d": when.strftime("%Y-%m-%d"), "t": when.strftime("%H:%M"), "h": is_home,
             "rival": pretty(away if is_home else home), "place": pretty(g("LOCATION"))}
        if g("GEO"):
            m["geo"] = g("GEO").replace(";", ",")
        if hg is not None:
            m["gf"], m["gc"] = (hg, ag) if is_home else (ag, hg)
        out.append(m)
    return sorted(out, key=lambda x: (x["d"], x["t"]))


def main():
    teams = []
    for path in sorted(glob.glob("data/teams/*.json")):
        t = json.load(open(path, encoding="utf-8"))
        url = t.pop("ics", None)
        if url:
            req = urllib.request.Request(url, headers={"User-Agent": "partits-bar/1.0"})
            t["matches"] = parse(urllib.request.urlopen(req, timeout=30).read().decode("utf-8"), t["me"])
        teams.append(t)
    try:
        old = json.load(open("data.json", encoding="utf-8"))
    except Exception:
        old = {}
    if old.get("teams") == teams:
        print("Sense canvis")
        return
    out = {"updated": dt.datetime.now(MAD).strftime("%Y-%m-%d"), "teams": teams}
    json.dump(out, open("data.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("data.json actualitzat")


if __name__ == "__main__":
    main()
