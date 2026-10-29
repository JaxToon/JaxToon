"""Generate GitHub profile cards (stats + top languages) as SVG.

Runs inside GitHub Actions with the built-in GITHUB_TOKEN, so it needs no
third-party service and no personal access token.

Writes four files into the output folder:
  stats.svg, stats-dark.svg, langs.svg, langs-dark.svg

Usage:
  GITHUB_TOKEN=... python profile_cards.py <username> <output_dir>
"""
import json
import os
import sys
import urllib.request
from html import escape

USER = sys.argv[1] if len(sys.argv) > 1 else "JaxToon"
OUT = sys.argv[2] if len(sys.argv) > 2 else "dist"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

# Notebook and markup bytes include outputs/images and swamp real code, so
# they are left out of the language card. Edit this list to taste.
EXCLUDE_LANGS = {"Jupyter Notebook", "HTML", "CSS", "TeX"}
TOP_N = 6
MIN_SHARE = 0.005  # hide languages under 0.5% of the total

THEMES = {
    "light": {"title": "#134E5E", "text": "#24292f", "muted": "#57606a",
              "accent": "#2E8B6E", "track": "#d0d7de"},
    "dark": {"title": "#71B280", "text": "#e6edf3", "muted": "#8b949e",
             "accent": "#71B280", "track": "#30363d"},
}

LANG_COLORS = {
    "Python": "#3572A5", "Jupyter Notebook": "#DA5B0B", "JavaScript": "#f1e05a",
    "TypeScript": "#3178c6", "HTML": "#e34c26", "CSS": "#563d7c", "Shell": "#89e051",
    "PowerShell": "#4F8FD6", "SQL": "#e38c00", "R": "#198CE7", "Go": "#00ADD8",
    "Java": "#b07219", "C++": "#f34b7d", "C": "#555555", "Dockerfile": "#384d54",
    "TeX": "#3D6117", "Makefile": "#427819", "PLpgSQL": "#336790",
}
FALLBACK = ["#71B280", "#134E5E", "#E0A458", "#8E7DBE", "#D46A6A", "#5DA9E9"]
FONT = "'Segoe UI', Ubuntu, 'Helvetica Neue', Helvetica, Arial, sans-serif"


def api(url, body=None):
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "profile-cards")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def collect():
    repos, page = [], 1
    while True:
        batch = api(f"https://api.github.com/users/{USER}/repos?per_page=100&page={page}&type=owner")
        repos += batch
        if len(batch) < 100:
            break
        page += 1
    repos = [r for r in repos if not r["fork"]]

    langs = {}
    for r in repos:
        for name, size in api(r["languages_url"]).items():
            if name not in EXCLUDE_LANGS:
                langs[name] = langs.get(name, 0) + size

    user = api(f"https://api.github.com/users/{USER}")
    commits = None
    try:
        q = {"query": "query($l:String!){user(login:$l){contributionsCollection{totalCommitContributions}}}",
             "variables": {"l": USER}}
        commits = api("https://api.github.com/graphql", q)["data"]["user"][
            "contributionsCollection"]["totalCommitContributions"]
    except Exception as e:  # GraphQL unavailable: leave the row out
        print("commit count skipped:", e)

    return {
        "repos": len(repos),
        "stars": sum(r["stargazers_count"] for r in repos),
        "followers": user.get("followers", 0),
        "commits": commits,
        "langs": langs,
    }


def fmt(n):
    return f"{n / 1000:.1f}k" if n >= 1000 else str(n)


def stats_rows(d):
    rows = [("Public repos", d["repos"]), ("Stars earned", d["stars"]),
            ("Followers", d["followers"])]
    if d["commits"] is not None:
        rows.insert(0, ("Commits (last 12 months)", d["commits"]))
    # A zero row draws the eye to a weak number; it reappears once it is > 0.
    return [(label, value) for label, value in rows if value or label == "Public repos"]


def top_langs(d):
    total = sum(d["langs"].values()) or 1
    top = [kv for kv in sorted(d["langs"].items(), key=lambda kv: -kv[1])
           if kv[1] / total >= MIN_SHARE][:TOP_N]
    return top, total


def card_height(d):
    """One height for both cards, so they line up side by side."""
    stats_h = 70 + 30 * len(stats_rows(d))
    langs_h = 100 + 25 * ((len(top_langs(d)[0]) + 1) // 2)
    return max(stats_h, langs_h, 130)


def stats_svg(d, t):
    rows = stats_rows(d)
    h = card_height(d)
    parts = [f'<text x="25" y="38" class="title">Firgy\'s GitHub</text>']
    for i, (label, value) in enumerate(rows):
        y = 75 + 30 * i
        parts.append(
            f'<circle cx="31" cy="{y - 5}" r="4" fill="{t["accent"]}"/>'
            f'<text x="45" y="{y}" class="label">{escape(label)}</text>'
            f'<text x="375" y="{y}" class="value" text-anchor="end">{fmt(value)}</text>')
    return wrap(400, h, t, "".join(parts))


def langs_svg(d, t):
    top, total = top_langs(d)
    shown = sum(v for _, v in top) or 1
    w, bar_w = 400, 350
    parts = [f'<text x="25" y="38" class="title">Most used languages</text>',
             f'<clipPath id="bar"><rect x="25" y="55" width="{bar_w}" height="10" rx="5"/></clipPath>',
             f'<rect x="25" y="55" width="{bar_w}" height="10" rx="5" fill="{t["track"]}"/>']
    x = 25.0
    for i, (name, size) in enumerate(top):
        seg = bar_w * size / shown
        color = LANG_COLORS.get(name, FALLBACK[i % len(FALLBACK)])
        parts.append(f'<rect clip-path="url(#bar)" x="{x:.2f}" y="55" width="{seg + 0.5:.2f}" height="10" fill="{color}"/>')
        x += seg
    for i, (name, size) in enumerate(top):
        col, row = i % 2, i // 2
        cx, cy = 30 + col * 180, 95 + row * 25
        color = LANG_COLORS.get(name, FALLBACK[i % len(FALLBACK)])
        parts.append(
            f'<circle cx="{cx}" cy="{cy - 4}" r="5" fill="{color}"/>'
            f'<text x="{cx + 12}" y="{cy}" class="label">{escape(name)} '
            f'<tspan class="muted">{100 * size / total:.1f}%</tspan></text>')
    return wrap(w, card_height(d), t, "".join(parts))


def wrap(w, h, t, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'role="img" font-family="{FONT}">'
        f'<style>.title{{font-size:17px;font-weight:600;fill:{t["title"]}}}'
        f'.label{{font-size:14px;fill:{t["text"]}}}.value{{font-size:14px;font-weight:600;fill:{t["text"]}}}'
        f'.muted{{fill:{t["muted"]}}}</style>{body}</svg>')


def main():
    if os.environ.get("MOCK"):
        data = json.loads(os.environ["MOCK"])
    else:
        data = collect()
    print(json.dumps({k: v for k, v in data.items() if k != "langs"}),
          "languages:", len(data["langs"]))
    os.makedirs(OUT, exist_ok=True)
    for mode, t in THEMES.items():
        suffix = "" if mode == "light" else "-dark"
        with open(f"{OUT}/stats{suffix}.svg", "w") as f:
            f.write(stats_svg(data, t))
        with open(f"{OUT}/langs{suffix}.svg", "w") as f:
            f.write(langs_svg(data, t))


if __name__ == "__main__":
    main()
