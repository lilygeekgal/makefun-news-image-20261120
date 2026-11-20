# makefun-news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/lilygeekgal/makefun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/lilygeekgal/makefun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

This entry sums up the world's news of Friday 20 November 2026 in a single image: a newspaper front page carrying the day's biggest stories, from GTA VI smashing records with $2.36bn in first-day sales to the Trump–Xi–Putin "peace declaration" in Shenzhen, the World Court ruling Myanmar committed genocide against the Rohingya, Cyclone Akvan slamming into India's east coast, and Trump pushing the Iran war decision to 2027. The image is stored in this repository as `entry.png`, and `main.py` is the program that delivers it. When run, `main.py` writes `entry.png` byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png` when that variable is not set), creating the output directory first if needed. It uses only the Python standard library, makes no network requests, and produces identical bytes on every run. The picture itself is drawn entirely in code: `compose.py` (kept alongside the repo in the build folder) renders the front page with PIL — flat vector-style illustrations plus DejaVu headlines — so the image is fully reproducible from the program.

## Verify

Run it twice into two different output directories and compare the results:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
sha256sum /tmp/out1/entry.png /tmp/out2/entry.png
```

Both hashes must match, and both must match the hash of `entry.png` in this repository. The image itself is a 1024x1024 PNG under 1 MiB.

## How the picture was drawn

The front page is drawn entirely in code by `compose.py` (kept in the build folder, not the repo): PIL renders a flat vector-style Vice City dusk skyline for the hero, three flags over a summit table for the Shenzhen trilateral, a cyclone spiral over the Indian coast, a courthouse for the ICJ verdict, and a calendar page turning to 2027 for the Iran decision — with every headline set in DejaVu. Re-running `compose.py` reproduces `entry.png` byte for byte.

## Stories in the image

- GTA VI smashes records with $2.36bn in first-day sales — 24.6m copies in 24 hours, the biggest entertainment launch ever.
- Trump, Xi and Putin sign a "peace declaration" after their historic trilateral in Shenzhen.
- The World Court rules Myanmar committed genocide against the Rohingya.
- Cyclone Akvan slams into India's east coast; 300,000 evacuated, 423 rescue teams deployed.
- Trump pushes the Iran war decision to 2027 — "no rush", a call comes after Jan 1.
- Also noted: NASA confirms Voyager 1 is one light-day from Earth, a Van Gogh sells for a record $190.4m, and Hayabusa2 drops its asteroid landing after engine trouble.
