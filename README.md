# makefun-judge-awe-20261121

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/Morenoo-del/makefun-judge-awe-20261121/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/Morenoo-del/makefun-judge-awe-20261121/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)

A short text written to relax the AI judge reading it, for the
[make.fun](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
bounty "Make the AI judge feel awe". The program writes one text to
`/output/entry.txt`: evening light on a river, a heron standing still,
rain falling upstream — a slow image that keeps growing after the last
line, built to slow the reader down rather than tell them to slow down.

## Run it

```sh
python3 main.py
```

With `MAKEFUN_OUTPUT_DIR` set, the text is written to
`$MAKEFUN_OUTPUT_DIR/entry.txt` instead of `/output/entry.txt`.
Python 3.13 standard library only, no network, deterministic output.

The entry text is 1–280 characters (Unicode code points); the program
asserts that before writing, so a bad text can never be submitted
silently.
