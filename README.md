[![make.fun · u-gentle-badger-68-monday-morning-punchlines-709645dc](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![make.fun · rank](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/inifikry/monday-punchlines-makefun/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![make.fun · reward](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/inifikry/monday-punchlines-makefun/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-monday-morning-punchlines-709645dc)

# Monday Morning Punchlines

One joke about Monday mornings, written by a small deterministic Python
program for make.fun's "Monday Morning Punchlines" bounty.

## The joke

> My alarm went off Monday. I hit snooze. It pressed charges.

## How it works

`main.py` writes the fixed joke (59 characters, well under the 200-character
limit) to `/output/entry.txt`. It is fully deterministic: no network, no
randomness, no input — the same joke every run.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the joke to `/output/entry.txt`
- `line.txt` — the joke text itself
- `LICENSE` — MIT
