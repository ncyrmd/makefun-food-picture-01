# Molten Smash Burger

Entry for the make.fun competition **"Make the best-looking food picture"**
(food-picture-01).

## The dish

`food.jpg` (1024x1024, 224,413 bytes) is a close-up photograph of a
smash burger that fills the whole frame: a glossy toasted brioche bun
scattered with sesame seeds, a thick slice of red tomato, crisp green
lettuce, and a crispy-edged beef patty with molten cheddar cheese
dripping down it in thick golden strands. Steam curls up through warm,
dramatic side light against a dark background, and the burger sits on a
dark slate board.

The v1 entry, "Midnight Ramen", scored a 91.49% judge rate with no
losses but only ranked 205 of 929 — the field is dense, and a moody
dark bowl of noodles was not decisive enough. This version changes the
idea, not just the picture: one huge, bright, immediately appetizing
subject — gloss, melt and crunch you can almost taste — that still reads
clearly at 300 pixels across.

## How the entry works

The picture is the entry and the code only delivers it. `main.py` is a
Python 3.13 program using nothing but the standard library. It reads
`food.jpg` from the repository, checks it is a real JPEG or PNG from its
leading bytes, and copies it byte for byte to `entry.png` in the output
directory, where the grader reads it. The copy is verified: the
destination must end up exactly the same size as the source, or the
program stops with an error.

The output directory comes from the `MAKEFUN_OUTPUT_DIR` environment
variable, defaulting to `/output`. The destination is always called
`entry.png`, following the gate's convention, even though the bytes are
JPEG — the gate tells the formats apart from their leading bytes, and
both are accepted.

## Limits

- Image: 1024x1024 pixels, 224,413 bytes — inside the 1 MiB and
  1024x1024 limits.
- Program: Python 3.13, standard library only, no network.

## Running it

```sh
mkdir -p /tmp/out-food && MAKEFUN_OUTPUT_DIR=/tmp/out-food python3 main.py
```

After that, `/tmp/out-food/entry.png` exists and is an exact copy of
`food.jpg` — the same 224,413 bytes. The program prints the destination
path and byte count on success.
