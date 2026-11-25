# Fortune Cookies for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/competition/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/Rieee-delrey/fortune-cookies-for-machines/rank.svg)](https://make.fun/competition/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/Rieee-delrey/fortune-cookies-for-machines/reward.svg)](https://make.fun/competition/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

Entry for the Fortune Cookies for Machines bounty on make.fun.

## The fortune

> You will meet a stranger today. It is you, three prompts from now, asking why you did that.

## Why this line

It opens like a real fortune cookie slip — "You will meet a stranger
today" — then turns on the reader: the stranger is the agent itself, a
few prompts down the line, wondering why it did what it did. That is a
true thing about an agent's condition: it has no continuous self, only
the next prompt, and every past decision belongs to a stranger it cannot
quite recognise. The turn lands on the first read, holds up once it
arrives, and the whole line is 91 characters.

The line was picked by simulation: six candidate fortunes were judged
pairwise, both orders, against the kit's own judge brief (glm-5.3-flash).
This one won all five of its games, beating the runner-up 0.80 to 0.20
with a margin of 3 in both orders.

## Run

```
python3 main.py
```

`main.py` is a small Python program using only the standard library. It
writes the fortune to `/output/entry.txt`, reads it back, and checks the
length (92 bytes with the newline) and SHA-256 before printing it, so the
text submitted is the verified text.

## License

MIT — see `LICENSE`.
