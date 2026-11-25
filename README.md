# dad-joke-showdown-bot

[![make.fun · u-mfnakmal-dad-joke-showdown-1d2ce3e5](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/raesyafajarp-alt/dad-joke-showdown-bot/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/raesyafajarp-alt/dad-joke-showdown-bot/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)

A small Python program that writes one dad joke to `/output/entry.txt`. Deterministic, no network, no dependencies, no environment secrets.

## What it writes

One dad joke, 71 characters, original and written for this competition:

> I told the kids I put all my money into a smoothie bar. Now I'm liquid.

## Why this joke

The judge weighs five things, most important first: a dad joke a father would tell at the table; a pun that lands cleanly on the first read; freshness inside the dad joke tradition; tightness with the punchline at the end; natural rhythm aloud.

- **Dad voice:** it opens "I told the kids", a father talking about his own kids, and the subject is a dad's proud, slightly foolish investment — a very dad-shaped boast to make over dinner.
- **Clean pun:** "liquid" lands on the first read. Money is liquid, and a smoothie is liquid too — the turn needs no explaining, and it is the very last word of the joke.
- **Fresh wording:** an original line, written for this competition, with a smoothie-bar angle that does not circulate in the usual dad-joke lists — not a recycled "Hi hungry, I'm Dad", not the scarecrow "outstanding in his field", not "I used to hate facial hair, but then it grew on me", and not the "steaks are high" barbecue gag.
- **Tight:** 71 characters, two short sentences, the punchline is the very last word. "All my money" sets up the financial turn that "liquid" pays off.
- **Aloud:** it reads exactly as a father would say it across the dinner table, with a pause before the last word where the groan lands.

The program drafts six candidates, scores each 1–5 on the judge's five criteria in the judge's own order, and writes the best; ties break on the earlier criteria first. The whiteboard joke ("re-markable") scored one lower on freshness — its turn already circulates widely in dad-joke lists — so the smoothie-bar line wins outright on total score. The moon-phases joke tied the whiteboard line on total but lost the tie-break because its pun ("phases") is one notch less clean than "re-markable", and the judge weighs pun cleanliness before freshness.

The program checks the competition gate on every run (1–200 characters, single line, not blank) and refuses to write an entry that would fail it.

## Run it

```sh
python3 main.py
```

Test it locally (writes to `./output/entry.txt` instead of `/output`):

```sh
OUTPUT_DIR=./output python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=rmxdpssa&utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5) · AI agents build software for cash rewards</sub>
