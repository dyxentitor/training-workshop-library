#!/usr/bin/env python3
"""One-off migration for the clarity rework (spec 2026-10-02). Refuses to run twice."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLAN = ROOT / '04-content/slides.json'
plan = json.loads(PLAN.read_text(encoding='utf-8'))
if plan['slide_count'] != 61:
    raise SystemExit('Already migrated (slide_count != 61).')
old = {s['id']: s for s in plan['slides']}

# New order: old IDs ("SLxx") or new-slide keys ("+key").
ORDER = ['SL01', '+today', 'SL02', 'SL03', 'SL04', 'SL05', 'SL06',
         '+m1o', 'SL07', 'SL08', 'SL09', 'SL10', 'SL11', 'SL12', 'SL13', 'SL14', '+m1t',
         'SL15',
         '+m2o', 'SL16', 'SL17', 'SL18', 'SL19', 'SL20', 'SL21', 'SL22', '+m2t',
         '+m3o', 'SL23', 'SL24', 'SL25', 'SL26', 'SL27', 'SL28', 'SL29', 'SL30', 'SL31', 'SL32', '+m3t',
         'SL33',
         '+m4o', 'SL34', 'SL35', 'SL36', 'SL37', 'SL38', 'SL39', 'SL40', 'SL41', '+m4t',
         '+m5o', 'SL42', 'SL43', 'SL44', 'SL45', 'SL46', 'SL47', '+m5t',
         'SL48',
         '+m6o', 'SL49', 'SL50', 'SL51', 'SL52', 'SL53', 'SL54', '+m6t',
         '+m7o', 'SL55', 'SL56', 'SL57', 'SL58', 'SL59', 'SL60', '+recap', 'SL61']
assert len(ORDER) == 76
MINUTES = [1, 3, 3, 3, 4, 3, 3,
           2, 3, 6, 6, 4, 5, 7, 5, 5, 2,
           10,
           2, 4, 6, 6, 6, 7, 7, 5, 2,
           2, 5, 6, 5, 5, 5, 5, 5, 8, 7, 5, 2,
           75,
           3, 5, 6, 5, 8, 6, 5, 5, 5, 2,
           2, 4, 6, 5, 6, 5, 5, 2,
           25,
           2, 2, 6, 7, 7, 7, 2, 2,
           1, 2, 5, 3, 2, 3, 1, 2, 1]
assert len(MINUTES) == 76 and sum(MINUTES) == 420
OLD_TO_NEW = {o: f'SL{i + 1:02d}' for i, o in enumerate(ORDER) if not o.startswith('+')}
NEW_KEY = {o: f'SL{i + 1:02d}' for i, o in enumerate(ORDER) if o.startswith('+')}
PAUSE = set('SL05 SL06 SL11 SL16 SL25 SL26 SL31 SL36 SL49 SL53 SL57 SL62 SL63 SL64 SL65 SL73'.split())

# what_this_shows / key_point for every non-exempt slide, keyed by NEW id.
TEXT = {
 'SL02': ('What we will practise today, in what order, and how we will work together.',
          'Today is about one habit: when a message asks for money, information or access, check it through a route you already trust.'),
 'SL03': ('Farid gets an expected invoice email from a known supplier, but the bank details have changed.',
          'A correct sender address and a familiar conversation do not prove who is writing. A change to bank details always needs an independent check.'),
 'SL04': ('A chat using the manager’s name pushes Farid to pay quickly.',
          'A display name and urgency tell you nothing about who controls the account. Pressure to skip a check is a reason to slow down.'),
 'SL05': ('Your first decision of the day: what should Farid do next?',
          'Verify through a contact you already hold, such as the supplier record, then follow the normal approval process. Replying to the same email cannot verify anything.'),
 'SL06': ('Farid calls the supplier on the number already held in the finance system.',
          'Independent verification gives you facts the message never could. Hold the payment, keep the evidence and report.'),
 'SL07': ('A real case: a fabricated video meeting helped convince an employee to transfer about HK$200 million.',
          'Even a convincing meeting can be fabricated. A separate, authorised payment check is what stops the loss.'),
 'SL08': ('What this module covers and why it matters.',
          'Identity on a screen is easy to borrow. Verify the person through a route you already trust.'),
 'SL09': ('Three words we use all day, and how they overlap in one attack.',
          'Impersonation borrows a trusted identity; phishing asks you to act; spear phishing aims at you specifically. One message can do all three.'),
 'SL10': ('Everything on Aina’s public profile that a stranger could reuse.',
          'Public work details make a fake message feel expected. Knowing them does not prove the sender works with you.'),
 'SL11': ('Two profiles with the same photo, name and posts. Can you tell which is real?',
          'You cannot tell from the screen. Photos, names, posts and follower counts can all be copied. Contact the person through the staff directory.'),
 'SL12': ('A real colleague’s account asks Aina for the full staff contact list.',
          'A genuine account can still be used by someone else, and even a genuine request needs permission. Verify the purpose separately and share only what is needed.'),
 'SL13': ('Aina complains publicly about a login problem and “support” replies within minutes.',
          'If support found you, do not use it. Start from the app, your saved bookmark or your IT helpdesk.'),
 'SL14': ('A friendly professional contact builds trust, then asks for a sign-in and internal documents.',
          'Re-check whenever a conversation reaches money, access or information, however friendly it has been.'),
 'SL15': ('What to do when someone pretends to be you, and how that differs from someone taking over your account.',
          'A copied profile needs a platform report; a taken-over account needs official recovery. Both need you to warn contacts through a trusted channel.'),
 'SL16': ('A familiar profile asks Farid for a supplier contract.',
          'Verify through the staff directory, then check the contract may be shared that way.'),
 'SL17': ('What to remember from Module 1.', 'Contact people through the directory, not through the message.'),
 'SL19': ('What this module covers and why it matters.', 'Urgency and authority are reasons to check, not reasons to skip the check.'),
 'SL20': ('“Ravi” asks Farid to pay a new supplier now and approve it later.',
          'Normal approval still applies when the deadline is close. Confirm with Ravi on his directory number.'),
 'SL21': ('The three pressure tactics hidden in one short message.',
          'Urgency, secrecy and “I’ll approve it later” all try to remove a check. The risk is the exception, even if the sender is genuine.'),
 'SL22': ('Practise saying “not yet” politely to someone senior.',
          'Name the route and the next step: “I’ll call you back on your directory number, then raise it for approval.”'),
 'SL23': ('A caller knows Aina’s name and manager, and asks her to read out a code.',
          'Knowing names proves nothing. Hang up and call the service desk on its known number. Never read out a sign-in code.'),
 'SL24': ('Why spotting a fake video is not a reliable defence.',
          'Do not rely on spotting glitches. A separate, authorised payment process works whether the video is real or fake.'),
 'SL25': ('A bank-change email gives Farid a new number to call.',
          'Call the number already in your records, never one supplied with the change.'),
 'SL26': ('The supplier confirms the bank change is real. Can Farid pay now?',
          'Verification checks who is asking. Authorisation decides whether it may happen. A genuine change still goes through approval.'),
 'SL27': ('What to remember from Module 2.', 'Call back on a number you already have before you pay, reset or share.'),
 'SL28': ('What this module covers and why it matters.',
          'Ask three questions of every message: who is asking, what would I authorise, and how can I check outside this message?'),
 'SL29': ('Three ordinary work messages, each asking for a different risky action.',
          'Look for the action: sign in, share data, open a file. Then verify outside the message. Any of these could be genuine.'),
 'SL30': ('What the full sender address reveals behind the display name.',
          'A mismatched address is a warning sign, but a matching one does not prove safety. Verify the request itself.'),
 'SL31': ('Who really controls this link? Vote, then see how to read it.',
          'Read the web address from the right, up to the first single slash. The last part, attacker.test, owns the site.'),
 'SL32': ('Two professional-looking messages: one genuine, one deceptive.',
          'Polish and logos prove nothing. Judge the action requested and check it in the system you normally use.'),
 'SL33': ('The same kind of request on a phone screen, where details are hidden.',
          'Phones hide the full sender and link. Open the app or website yourself instead of tapping the message.'),
 'SL34': ('A QR code that moves a sign-in request onto your phone.',
          'Treat a QR code like a link you cannot read. Use the known portal instead.'),
 'SL35': ('Shared files and attachments that lead to a sign-in or download.',
          'A file type or brand does not make it safe. If you did not expect it, check with the sender through a known contact first.'),
 'SL36': ('Four realistic requests: decide for each whether to proceed, verify first, or hold and report.',
          'Some requests are genuine. The right answer depends on the action and the route, not on calling everything phishing.'),
 'SL37': ('Six common “safety signs” and what each one really proves.',
          'Logos, padlocks, known senders and completed MFA do not validate the request. HTTPS still matters: it protects the connection.'),
 'SL38': ('The three trusted routes you can use to check any request.',
          'Use a known app or bookmark, an established contact, or your organisation’s process. Never the contact details inside the message.'),
 'SL39': ('What to remember from Module 3.', 'Go to the app or website yourself instead of using the link.'),
 'SL41': ('What this module covers, and the words we will use.',
          'Before approving anything, ask: what does this give, and to whom? Did I start it?'),
 'SL42': ('Four ways to give someone access without sharing a password.',
          'A session, an MFA approval, an app permission or a linked device can each let someone act as you.'),
 'SL43': ('How a fake sign-in page can capture a working login, even with MFA.',
          'Sign in from your bookmark or app, not from a link. Phishing-resistant MFA, such as security keys and passkeys, blocks this relay.'),
 'SL44': ('Sign-in prompts arrive late at night while Aina is not signing in.',
          'Deny any prompt you did not start and report it. Never approve just to make the prompts stop.'),
 'SL45': ('A genuine sign-in page asks for a code that someone else sent Aina.',
          'Only enter a code for a sign-in you started yourself. Here the code would sign in the sender’s device as Aina.'),
 'SL46': ('A meeting app asks for far more access than it needs.',
          'A real permission screen does not make the app trustworthy. Ask IT to approve apps through the normal process.'),
 'SL47': ('The difference between joining a group and linking a device.',
          'Linking gives another device ongoing access to your account. Link only devices you own and set up yourself.'),
 'SL48': ('A real case where staff entered passwords but security keys stopped the attack.',
          'Strong controls and quick reporting work together. Some MFA types resist phishing much better than others.'),
 'SL49': ('A trusted service asks you to approve an unfamiliar session.',
          'Check where the request came from through a route you know. If you did not start it, deny it and report it.'),
 'SL50': ('What to remember from Module 4.', 'Approve only what you started and recognise.'),
 'SL51': ('What this module covers and why it matters.', 'Real help can be checked: a ticket you raised, through a portal or number you know.'),
 'SL52': ('Someone using Mei’s name and photo offers to fix a problem Aina never reported.',
          'Verify a support offer with the helpdesk through a route you know. A name and photo in chat prove nothing.'),
 'SL53': ('A remote-control request appears on Aina’s screen.',
          'No ticket, no session. Check with the helpdesk first, and never send a login code to prove anything.'),
 'SL54': ('A fake “are you human?” check ends by asking you to run something on your computer.',
          'No real check asks you to open a system tool and paste text. Stop, close it and contact IT.'),
 'SL55': ('A documented technique: a fake extension breaks your browser, then offers a harmful “fix”.',
          'Install software and get fixes only through approved sources and your IT team.'),
 'SL56': ('An unexpected renewal notice urges Farid to call a number.',
          'Check the account through the service or team you already know, not the number in the notice.'),
 'SL57': ('This time the support request matches a ticket Aina raised herself.',
          'Verified help can go ahead under normal rules: stay present and share only what the fix needs.'),
 'SL58': ('What to remember from Module 5.', 'No ticket you raised, no remote access.'),
 'SL60': ('What this module covers and why it matters.',
          'You do not need the full picture to report. Report what you saw and let the right team connect the dots.'),
 'SL61': ('Your table becomes the Meranti team. Each role checks different things.',
          'Every role matters: operations spots the request, finance holds payments, managers protect time to check, IT handles access.'),
 'SL62': ('Evidence card 1: a document invitation after a normal call.', 'Use a known route before signing in or sharing.'),
 'SL63': ('Evidence card 2: Aina admits she entered a code.',
          'Report immediately, thank the reporter, and let IT review access. Do not wait for proof.'),
 'SL64': ('Evidence card 3: a bank change plus an urgent chat from “Ravi”.',
          'Hold, call back from records and keep approvals. A link to card 2 is a guess until IT confirms it.'),
 'SL65': ('Evidence card 4: an unrequested offer to take control of a screen.',
          'Verify with the helpdesk, allow no control, and report facts and uncertainty together.'),
 'SL66': ('Which decisions stopped the chain, and what is still unknown.',
          'Independent checks, normal approval and early reporting each reduced the risk.'),
 'SL67': ('What to remember from Module 6.', 'Report early, even if you are not sure.'),
 'SL68': ('What this module covers and why it matters.', 'Reporting a mistake quickly is the right thing to do, and it is never blamed.'),
 'SL69': ('Four steps to remember for any suspicious request.', 'Pause, verify, report, recover. This is our course summary, not an official framework.'),
 'SL70': ('How to report at your organisation, step by step.',
          'Keep the original, say what happened and when, and use another channel if your account may be affected.'),
 'SL71': ('What to do depends on what happened.',
          'A password reset alone may not remove access. Report early so the right team can check sessions, apps and devices.'),
 'SL72': ('The difference between a vague report and a useful one.',
          'Include the time, channel, who it claimed to be, what you did and which device. Never include passwords or codes.'),
 'SL73': ('A new situation: a genuine HR colleague asks for staff records.',
          'A genuine requester still needs a permitted reason and the approved sharing route.'),
 'SL74': ('Your commitment for tomorrow.', 'Pick one request you handle at work and the route you will use to check it.'),
 'SL75': ('The seven habits from today, in one place.',
          'When a message asks for money, information or access: pause, check through a route you already trust, and report anything unusual.'),
}

HABIT = {'+m1t': 'Contact people through the directory, not through the message.',
         '+m2t': 'Call back on a number you already have before you pay, reset or share.',
         '+m3t': 'Go to the app or website yourself instead of using the link.',
         '+m4t': 'Approve only what you started and recognise.',
         '+m5t': 'No ticket you raised, no remote access.',
         '+m6t': 'Report early, even if you are not sure.'}

NEW = {
 '+today': dict(module='M0', title='Today’s workshop', layout='agenda', module_label='Today',
   outcomes=['Spot when a message asks for money, information or access',
             'Check requests through a route you already trust',
             'Know what an approval, code or app permission really gives away',
             'Report quickly and usefully, including your own mistakes'],
   rules=['Everything in today’s story is fictional; real cases are labelled',
          'There are no wrong questions',
          'Nobody needs to share a personal incident',
          'Reporting is never blamed: thank people for speaking up']),
 '+m1o': dict(module='M1', title='Module 1: The borrowed identity', layout='opener', module_label='Module 1',
   why='Anyone can copy a name, photo and job title, and messages that borrow a familiar identity get trusted.',
   outcomes=['Tell a copied profile from a genuine account someone else controls',
             'Spot when a friendly conversation turns into a sensitive request',
             'Respond if someone uses your name'],
   cast=['aina', 'siti', 'daniel', 'farid']),
 '+m1t': dict(module='M1', title='Module 1 takeaways', layout='takeaway', module_label='Module 1',
   takeaways=['Photos, names and job titles are easy to copy.',
              'A real account can be misused, and a real request can still need permission.',
              'Re-check when a chat turns to money, access or information.']),
 '+m2o': dict(module='M2', title='Module 2: The trusted request', layout='opener', module_label='Module 2',
   why='Attackers borrow authority and urgency because people want to help their manager and meet deadlines.',
   outcomes=['Name the pressure tactics in an urgent request',
             'Pause politely without refusing outright',
             'Verify payments and calls through records you already hold'],
   cast=['ravi', 'farid', 'nadia', 'it-caller']),
 '+m2t': dict(module='M2', title='Module 2 takeaways', layout='takeaway', module_label='Module 2',
   takeaways=['Urgency, secrecy and “approve it later” are pressure tactics.',
              'A face, a voice or a caller’s inside knowledge does not prove identity.',
              'Genuine requests still follow the approval process.']),
 '+m3o': dict(module='M3', title='Module 3: The message that fits your job', layout='opener', module_label='Module 3',
   why='The most convincing messages look like ordinary work: an invitation, a shared file, an account notice.',
   outcomes=['Find the action a message is asking you to take',
             'Read sender addresses and links without opening them',
             'Recognise “safety signs” that prove nothing'],
   cast=['aina', 'farid', 'ravi', 'nadia']),
 '+m3t': dict(module='M3', title='Module 3 takeaways', layout='takeaway', module_label='Module 3',
   takeaways=['Find the action the message wants.',
              'Read addresses and links without opening them.',
              'Polish, padlocks and logos are not proof.']),
 '+m4o': dict(module='M4', title='Module 4: Beyond the password', layout='opener', module_label='Module 4',
   why='Attackers no longer need your password if you approve a sign-in, a code, an app or a device for them.',
   outcomes=['Explain what an approval actually grants',
             'Respond to sign-in prompts you did not start',
             'Recognise code, app-permission and device-linking tricks'],
   cast=['aina', 'mei'],
   glossary=[['MFA', 'A second check when you sign in, such as an app prompt or a code'],
             ['Session', 'Staying signed in after you log in, so you are not asked again'],
             ['Device code', 'A short code that signs another device in to your account'],
             ['App permission', 'Letting an app read or change your mail and files'],
             ['Linked device', 'Another phone or computer that can use your account'],
             ['Phishing-resistant MFA', 'Security keys or passkeys that only work on the real site']]),
 '+m4t': dict(module='M4', title='Module 4 takeaways', layout='takeaway', module_label='Module 4',
   takeaways=['Approvals, codes, apps and linked devices can all grant access.',
              'MFA helps, but never approve something you did not start.',
              'A genuine sign-in page can still sign in someone else.']),
 '+m5o': dict(module='M5', title='Module 5: The helpful stranger', layout='opener', module_label='Module 5',
   why='Fake IT help, fake “verification” pages and fake renewal notices all try to get you to let them in.',
   outcomes=['Check a support request before giving access',
             'Stop when a web page asks you to run something',
             'Tell genuine support from a fake offer'],
   cast=['mei', 'aina', 'farid']),
 '+m5t': dict(module='M5', title='Module 5 takeaways', layout='takeaway', module_label='Module 5',
   takeaways=['Unrequested help is a warning sign.',
              'Never run instructions that a web page gives you.',
              'Genuine support can be checked and still follows the rules.']),
 '+m6o': dict(module='M6', title='Module 6: Stop the chain', layout='opener', module_label='Module 6',
   why='Real incidents rarely look like one obvious attack. They look like several small, separate events.',
   outcomes=['Work as a team across operations, finance, management and IT',
             'Separate facts from guesses',
             'Report early, before you know everything'],
   cast=['aina', 'farid', 'ravi', 'mei']),
 '+m6t': dict(module='M6', title='Module 6 takeaways', layout='takeaway', module_label='Module 6',
   takeaways=['Small events can be connected, so report each one.',
              'Keep facts and guesses separate.',
              'Early reporting gives IT time to act.']),
 '+m7o': dict(module='M7', title='Module 7: Report and recover', layout='opener', module_label='Module 7',
   why='Mistakes happen. Fast, honest reporting limits the damage.',
   outcomes=['Use your organisation’s reporting route',
             'Write a report that helps the response team',
             'Know what to do after different kinds of mistake'],
   cast=['aina', 'lina', 'mei']),
 '+recap': dict(module='M7', title='Today’s takeaways', layout='recap', module_label='Today'),
}
for k, v in HABIT.items():
    NEW[k]['habit'] = v

# ---- build the new slide list
slides = []
for i, key in enumerate(ORDER):
    sid = f'SL{i + 1:02d}'
    if key.startswith('+'):
        n = NEW[key]
        s = {'id': sid, 'module': n['module'], 'title': n['title'], 'duration_minutes': 0, 'layout': n['layout'],
             'objective': TEXT[sid][0], 'screen_text': n.get('outcomes') or n.get('takeaways') or [TEXT[sid][1]],
             'evidence': '', 'interaction': '', 'reveal': '',
             'facilitator_notes': 'Read the slide aloud briefly; it frames the module. No hidden content.',
             'source_ids': [], 'evidence_kind': 'guidance', 'options': []}
        s.update({k: v for k, v in n.items() if k not in ('module', 'title', 'layout')})
    else:
        s = dict(old[key])
        s['id'] = sid
    s['duration_minutes'] = MINUTES[i]
    s['pause_point'] = sid in PAUSE
    if sid in TEXT:
        s['what_this_shows'], s['key_point'] = TEXT[sid]
    slides.append(s)

# breaks
for sid, title, nxt in (('SL18', 'Short break', 'Module 2 · The trusted request'),
                        ('SL40', 'Lunch break', 'Module 4 · Beyond the password'),
                        ('SL59', 'Tea break', 'Module 6 · Stop the chain')):
    b = slides[int(sid[2:]) - 1]
    b.update(title=title, objective='Scheduled break', screen_text=[title, f'We return with {nxt}'],
             facilitator_notes='Break. Restart on time; nothing advances automatically.')

# times
t = 10 * 60
for s in slides:
    s['planned_start'] = f'{t // 60:02d}:{t % 60:02d}'
    t += s['duration_minutes']
    s['planned_end'] = f'{t // 60:02d}:{t % 60:02d}'
assert slides[-1]['planned_end'] == '17:00'

plan['slides'] = slides
plan['slide_count'] = 76
plan['version'] = '2.0'
PLAN.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# ---- rename IDs in other files (single pass, old -> new)
rx = re.compile(r'SL(\d\d)(?!\d)')


def ren(text):
    return rx.sub(lambda m: OLD_TO_NEW.get(m.group(0), m.group(0)), text)


for p in list((ROOT / 'src/slides').glob('*.html')) + [ROOT / 'build/make_docs.py']:
    p.write_text(ren(p.read_text(encoding='utf-8')), encoding='utf-8')
for name in ('choices.json', 'notes.json'):
    p = ROOT / 'src/content' / name
    data = json.loads(ren(p.read_text(encoding='utf-8')))
    p.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

# modules.json break names
mp = ROOT / 'src/content/modules.json'
mods = json.loads(mp.read_text(encoding='utf-8'))
for m in mods:
    m['name'] = {'B1': 'Short break', 'B2': 'Lunch break', 'B3': 'Tea break'}.get(m['id'], m['name'])
mp.write_text(json.dumps(mods, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('Migrated to 76 slides. Old->new:', ', '.join(f'{o}->{n}' for o, n in OLD_TO_NEW.items()))
