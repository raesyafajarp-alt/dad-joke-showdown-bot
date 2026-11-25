#!/usr/bin/env python3
"""dad-joke-showdown-bot — Dad Joke Showdown (make.fun).

Writes exactly one dad joke of at most 200 characters to /output/entry.txt.

The competition gate: the file must be UTF-8 text of 1 to 200 characters,
not only white space. The house judge then compares entries two at a time
and weighs, most important first:

  1. Is a dad joke a father would tell at the table, within 200
     characters, and loses to any dad joke.
  2. Lands its pun cleanly, so the turn is understood on the first read
     without anyone explaining it.
  3. Feels fresh rather than a joke told a thousand times, while staying
     inside the dad joke tradition.
  4. Is tight, with every word earning its place and the punchline
     arriving at the end.
  5. Reads naturally aloud, with a rhythm a father could deliver across
     a dinner table.

The program drafts several original candidates, scores each one 1-5 on
those five criteria (in the judge's own order), and writes the best.
Ties break on the earlier criteria first, then on the shorter text.
The choice is deterministic: no randomness, no network, no environment
secrets, no reading anything outside this repository.

The winning joke:

  "I told the kids I put all my money into a smoothie bar.
   Now I'm liquid."

Why this line works, criterion by criterion:

  * Dad joke, told at the table (criterion 1): it opens "I told the
    kids", a father talking about his own kids, and the subject is a
    dad's proud, slightly foolish investment — a very dad-shaped
    boast to make over dinner.
  * Clean pun (criterion 2): "liquid" lands on the first read.
    Money is liquid, and a smoothie is liquid too — the turn needs
    no explaining, and it is the very last word of the joke.
  * Fresh (criterion 3): an original line, written for this
    competition, with a smoothie-bar angle that does not circulate
    in the usual dad-joke lists. It is not a recycled "Hi hungry,
    I'm Dad", not the scarecrow "outstanding in his field", not
    "I used to hate facial hair, but then it grew on me", and not
    the "steaks are high" barbecue gag.
  * Tight (criterion 4): 71 characters, two short sentences, and the
    punchline is the very last word. Nothing in the setup is wasted:
    "all my money" sets up the financial turn that "liquid" pays off.
  * Aloud (criterion 5): it reads exactly as a father would say it
    across the dinner table, with a pause before the last word where
    the groan lands.

Alternatives considered and rejected while writing this entry:

  * The whiteboard joke — "I told my kids I'm a big fan of
    whiteboards. They're quite re-markable." The pun is instant and
    the line is tight, but "re-markable" on a whiteboard already
    circulates widely in dad-joke lists, so it scores one notch
    lower on freshness than the smoothie-bar line, and the judge
    weighs freshness ahead of tightness and delivery.
  * The moon joke — "My daughter asked if the moon ever gets tired.
    I said no, it just phases in and out." Same total score, but its
    pun is one notch less clean: "phases" needs a half-second of
    thought, where "re-markable" is instant, and the judge weighs
    pun cleanliness before freshness, so the whiteboard line wins
    the tie.
  * The stairs joke — "I told the kids the stairs are my favourite
    exercise. They really step up." Clean and tight, but "step up"
    is a flatter turn than "re-markable": it leans on an idiom
    rather than a word that is itself the joke.
  * The vacuum joke — "I told my son the vacuum cleaner and I had a
    falling out. It just keeps sucking up to me." The "sucking up"
    turn is good, but the setup is longer and the pun is a little
    cruder; it reads less like a line told at the dinner table.
  * The calendar joke — "I told my wife the calendar's days are
    numbered. She said that's literally what a calendar is." Funny,
    but the turn is the wife's reply rather than a pun of the dad's
    own, so it scores lower on the pun criterion the judge weighs
    second.

The gate check below runs on every execution and refuses to write an
entry that would fail the 1-200 character gate, so a bad edit can
never silently ship.

Run it with:  python3 main.py
Test it with:  OUTPUT_DIR=./output python3 main.py
"""

import os
import sys

# Each candidate: (text, scores 1-5 for the judge's five criteria, in order)
CANDIDATES = [
    (
        "I told the kids I put all my money into a smoothie bar. "
        "Now I'm liquid.",
        (5, 5, 5, 5, 5),  # dad voice, clean pun, fresh, tight, aloud
    ),
    (
        "I told my kids I'm a big fan of whiteboards. "
        "They're quite re-markable.",
        (5, 5, 4, 5, 5),  # dad voice, clean pun, fresh, tight, aloud
    ),
    (
        "My daughter asked if the moon ever gets tired. "
        "I said no, it just phases in and out.",
        (5, 4, 5, 5, 5),
    ),
    (
        "I told the kids the stairs are my favourite exercise. "
        "They really step up.",
        (5, 4, 4, 5, 5),
    ),
    (
        "I told my son the vacuum cleaner and I had a falling out. "
        "It just keeps sucking up to me.",
        (5, 4, 4, 4, 4),
    ),
    (
        "I told my wife the calendar's days are numbered. "
        "She said that's literally what a calendar is.",
        (4, 3, 4, 4, 4),
    ),
]

# Best total, ties broken on the earlier criteria first, then shorter text.
BEST = max(
    CANDIDATES,
    key=lambda c: (sum(c[1]), c[1], -len(c[0])),
)
JOKE = BEST[0]

# The gate: 1 to 200 characters, counted as Unicode code points,
# and not only white space. A single dad joke: no newline inside.
length = len(JOKE)
if length < 1 or length > 200:
    raise SystemExit(f"Joke is {length} characters; must be 1-200.")
if not JOKE.strip():
    raise SystemExit("Joke must not be only white space.")
if "\n" in JOKE or "\r" in JOKE:
    raise SystemExit("Joke must be a single line.")

out_dir = os.environ.get("OUTPUT_DIR", "/output")
out_path = os.path.join(out_dir, "entry.txt")

try:
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(JOKE)
except OSError:
    # Fall back to a local output directory when /output is not writable
    # (for example when running the entry by hand outside the sandbox).
    out_path = os.path.join("output", "entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(JOKE)

print(f"Wrote {length} characters to {out_path}")
print(JOKE)
sys.exit(0)
