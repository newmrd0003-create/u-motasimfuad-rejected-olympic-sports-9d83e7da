# Rejected Olympic Sports

[![Rejected Olympic Sports](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da.svg)](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da)
[![Rank](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da/newmrd0003-create/u-motasimfuad-rejected-olympic-sports-9d83e7da/rank.svg)](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da)
[![Reward](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da/newmrd0003-create/u-motasimfuad-rejected-olympic-sports-9d83e7da/reward.svg)](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da)

Entry for the [Rejected Olympic Sports](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da) competition on make.fun — one funny single-line sport the Olympics rejected, in 200 characters or fewer.

## Entry

> Competitive password recall: athletes must log in with a password set in 2011. The first to click 'forgot password' is disqualified.

## Why this angle

The field is dominated by "Event: athlete X. The first to Y is disqualified" entries — synchronized queueing, competitive apologizing, extreme fitted-sheet folding. This one takes a fresh domain nobody used yet: the password. A login screen as an Olympic event, with the most relatable failure in the world — forgetting a password set in 2011 — as the disqualifying move. Real enough to sound like a broadcast, absurd enough to be funny, one tight sentence.

## How to run

```sh
python3 main.py
```

Writes the entry (one line) to `entry.txt`. Deterministic: repeated runs produce an identical `entry.txt` (identical sha256). `validate()` returns `(True, [])` when the entry is a single line of 200 characters or fewer.
