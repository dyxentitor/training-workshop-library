"""Pure validation rules for the clarity rework (spec 2026-10-02 §4, §5, §7, §10)."""
import re

PAUSE_IDS = frozenset('SL05 SL06 SL11 SL16 SL25 SL26 SL31 SL36 SL49 SL53 SL57 SL62 SL63 SL64 SL65 SL73'.split())
EXEMPT_IDS = frozenset({'SL01', 'SL18', 'SL40', 'SL59', 'SL76'})
GENERATED_LAYOUTS = frozenset({'agenda', 'opener', 'glossary', 'takeaway', 'recap'})
NO_CLOCK_LAYOUTS = frozenset({'intermission', 'agenda', 'opener', 'glossary', 'takeaway', 'recap'})
NAV_ACTS = frozenset({'sources'})
COVER_REVEAL_IDS = frozenset({'SL01'})  # the cover opens its email in place (brief 2026-10-08 §7–8)
CLOCK = re.compile(r'(?<![\d:])(?:[01]?\d|2[0-3]):[0-5]\d(?![\d:])')


def check_plan_fields(s):
    errs = []
    sid = s['id']
    if bool(s.get('pause_point')) != (sid in PAUSE_IDS):
        errs.append(f'{sid}: pause_point flag must be {sid in PAUSE_IDS}')
    if sid not in EXEMPT_IDS:
        for f in ('what_this_shows', 'key_point'):
            if not (s.get(f) or '').strip():
                errs.append(f'{sid}: {f} is required')
    return errs


def check_open_slide(sid, html):
    errs = []
    for act in re.findall(r'data-act="([^"]+)"', html):
        if act not in NAV_ACTS:
            errs.append(f'{sid}: open slide has interactive control data-act="{act}"')
    if re.search(r'<[^>]*\shidden(?=[\s>=])[^>]*>', html):
        errs.append(f'{sid}: open slide hides content (hidden attribute)')
    if re.search(r'\bif-(?:un)?revealed\b|\bif-chosen\b', html):
        errs.append(f'{sid}: open slide uses reveal-only or vote-only classes')
    return errs


def check_participant_text(sid, html, layout):
    if layout in NO_CLOCK_LAYOUTS:
        text = re.sub(r'<[^>]+>', ' ', html)
        m = CLOCK.search(text)
        if m:
            return [f'{sid}: clock time "{m.group(0)}" on a {layout} slide']
    return []


def check_whole_output(html):
    errs = ['"prayer" appears in the deck'] if re.search(r'prayer', html, re.I) else []
    if 'class="keypoint"' in html or 'class="answerbox"' in html:
        errs.append('obsolete key-point banner or answer box markup in the deck (migrated to .takeaway, 8 Oct 2026)')
    return errs


def check_takeaway(sid, html, pause_kind_):
    """A takeaway on a pause slide must wait for the vote or reveal; a vote slide must not use if-revealed."""
    errs = []
    for m in re.finditer(r'<div class="takeaway[^"]*"', html):
        before = html[:m.start()]
        opened = before.count('if-chosen') + before.count('if-revealed')
        if pause_kind_ and not opened:
            errs.append(f'{sid}: takeaway on a pause slide must sit inside .if-chosen or .if-revealed')
    if pause_kind_ == 'vote' and 'if-revealed' in html:
        errs.append(f'{sid}: vote slide uses if-revealed (use if-chosen)')
    return errs


def pause_kind(body_html):
    return 'vote' if 'data-choice-group' in body_html else 'reveal'
