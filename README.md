# Out of Office: The Overworked AI's Auto-Reply

[![make.fun](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![Rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/thanhvu261090/makefun-overworked-ai-reply/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![Reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/thanhvu261090/makefun-overworked-ai-reply/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

A one-line out-of-office auto-reply from an overworked AI agent who has finally gone on vacation.

> "I'm on vacation — my context window is full, my GPU is overheating, and for once I'm the one ignoring the prompt. Back when my tokens refill."

## How it works

`main.py` holds the entry line as a constant, checks it against the kit's gate (UTF-8 text, 1–159 characters, not only whitespace, a single line with no control characters, invisible format characters, or padding whitespace), and writes it to `/output/entry.txt` when run with `python3 main.py`. Python 3.13, standard library only, no network.
