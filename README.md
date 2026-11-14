# Midnight Ramen

Entry for the make.fun competition **"Make the best-looking food picture"**
(food-picture-01).

## What you are looking at

`food.jpg` (1024x1024) is a moody, premium-restaurant-style photograph of
a bowl of ramen at night: noodles lifted high on chopsticks, glossy with
broth, slices of chashu pork, a soft-boiled egg cut open to a jammy yolk,
scattered green onions and a sheet of nori, all in a dark speckled bowl
with steam curling up into a dark background under warm, dramatic side
light.

## What the code does

The picture is the entry; the code just delivers it. `main.py` is a
Python 3.13 program that depends on nothing but the standard library. It
takes `food.jpg` from the repository and copies it, byte for byte, to
`entry.png` inside the output directory, which is where the grader looks
for it.

Where the output goes is controlled by the `MAKEFUN_OUTPUT_DIR`
environment variable. When it is not set, the program uses `/output`.

## Running it

```sh
mkdir -p /tmp/out-food && MAKEFUN_OUTPUT_DIR=/tmp/out-food python3 main.py
```

After that command, `/tmp/out-food/entry.png` exists and is an exact copy
of `food.jpg` — same 220,380 bytes. The program also checks the copy
itself and reports the destination path and byte count on success.
