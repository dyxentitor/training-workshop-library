"""HTML for slides generated from slides.json fields: agenda, module opener, glossary, module takeaway, day recap.

Takeaways (8 Oct 2026): the agenda, glossary and recap carry their teaching point as a .takeaway block inside
the content column; module openers carry none (their lesson lives on the next teaching slide); the takeaway
layout's habit panel is its own takeaway."""
import html
from avatars import cast_html


def e(x):
    return html.escape(str(x), quote=True)


def takeaway(main, label='Remember', acts=(), note=''):
    """The reusable takeaway block: optional teal label, one statement, supporting lines."""
    h = '<div class="takeaway">'
    if label:
        h += f'<p class="tlabel">{e(label)}</p>'
    h += f'<p class="tmain">{e(main)}</p>'
    if acts:
        h += '<ul class="tacts">' + ''.join(f'<li>{e(a)}</li>' for a in acts) + '</ul>'
    if note:
        h += f'<p class="tnote">{e(note)}</p>'
    return h + '</div>'


def _after_colon(text):
    """The clause after a leading 'Today is about one habit:' style lead-in, capitalised."""
    rest = text.partition(': ')[2] or text
    return rest[:1].upper() + rest[1:]


def _split_point(text):
    """First sentence as the statement, the rest as one supporting line."""
    parts = [x.strip() for x in text.replace('? ', '?\x00').replace('. ', '.\x00').split('\x00') if x.strip()]
    return parts[0], ' '.join(parts[1:])


def _ul(items, cls=''):
    return f'<ul class="{cls}">' + ''.join(f'<li>{e(i)}</li>' for i in items) + '</ul>'


def _ol(items, cls=''):
    return f'<ol class="{cls}">' + ''.join(f'<li>{e(i)}</li>' for i in items) + '</ol>'


def render_generated(s, modules, habits):
    sid, lay = s['id'], s['layout']
    sub = '' if lay in ('opener', 'takeaway') else f'<p class="sub">{e(s["what_this_shows"])}</p>'
    head = (f'<p class="kicker">{e(s.get("module_label", "Today"))}</p>'
            f'<h1 id="{sid}-title">{e(s["title"])}</h1>{sub}')
    if lay == 'agenda':
        agenda = ''.join(
            f'<li class="{"brk" if m["kind"] == "break" else ""}">'
            f'{"" if m["kind"] == "break" else e(("Opening" if m["id"] == "M0" else "Module " + m["id"][1:]) + " · ")}{e(m["name"])}</li>'
            for m in modules)
        return (f'<div class="gen agenda"><div>{head}<p class="eyebrow">Today you will be able to</p>{_ul(s["outcomes"], "outcomes")}'
                f'<p class="eyebrow">How we work today</p>{_ul(s["rules"], "rules")}</div>'
                f'<div class="scene"><p class="eyebrow">The day</p><ul class="daylist">{agenda}</ul>'
                f'{takeaway(_after_colon(s["key_point"]), "One habit for today")}</div></div>')
    if lay == 'opener':
        gloss = ''
        if s.get('glossary'):
            gloss = ('<p class="eyebrow">Words we will use</p><dl class="glossary">'
                     + ''.join(f'<dt>{e(t)}</dt><dd>{e(d)}</dd>' for t, d in s['glossary']) + '</dl>')
        return (f'<div class="gen opener"><div>{head}<p class="eyebrow">Why this matters</p><p class="why">{e(s["why"])}</p>'
                f'<p class="eyebrow">Who you will meet</p>{cast_html(s["cast"])}</div>'
                f'<div class="scene"><p class="eyebrow">By the end you will be able to</p>{_ul(s["outcomes"], "outcomes")}{gloss}</div></div>')
    if lay == 'glossary':                        # SL41B: the module's terms on their own slide (readability rework, 8 Oct 2026)
        dl = '<dl class="glossary large">' + ''.join(f'<dt>{e(t)}</dt><dd>{e(d)}</dd>' for t, d in s['glossary']) + '</dl>'
        main, note = _split_point(s['key_point'])
        return f'<div class="gen terms"><div>{head}{takeaway(main, "", note=note)}</div><div class="scene">{dl}</div></div>'
    if lay == 'takeaway':
        return (f'<div class="gen takeaway"><div>{head}</div><div class="scene">{_ol(s["takeaways"], "tlist")}'
                f'<div class="habit"><p class="eyebrow">Your habit from this module</p><p class="habittext">{e(s["habit"])}</p></div></div></div>')
    if lay == 'recap':
        rows = ''.join(f'<li><span class="hmod">{e(m)}</span><span>{e(h)}</span></li>' for m, h in habits)
        main, note = s['key_point'].partition(': ')[0] + ':', s['key_point'].partition(': ')[2]
        return (f'<div class="gen recap"><div>{head}{takeaway(main, "One habit", note=note)}</div><div class="scene"><p class="eyebrow">Seven habits</p>'
                f'<ol class="habits">{rows}</ol></div></div>')
    raise ValueError(f'{sid}: unknown generated layout {lay}')
