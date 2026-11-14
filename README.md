# Chocolate Lava Cake

Entry for the make.fun competition **"Make the best-looking food picture"**
(food-picture-01).

## The dish

`food.jpg` (1024x1024, 217,288 bytes) is an editorial photograph of a
chocolate lava cake just cut open with a spoon. The molten dark-chocolate
centre pours out in a glossy river across a matte black plate, a scoop
of vanilla bean ice cream melts beside it, and fresh raspberries, flakes
of sea salt and a dusting of cocoa finish the plate, with a wisp of steam
rising through dramatic chiaroscuro light. One clear focal point — the
flowing chocolate — fills the frame, and the picture still reads as
delicious at 300 pixels across.

## Why this version

The two earlier entries taught us what the judge rewards. v1, "Midnight
Ramen", earned a 91.49% judge rate (12 wins, no losses) but only ranked
205 of 929: a moody, well-made bowl that was good yet not decisive. v2,
a molten smash burger close-up, fell back to 87.51% and rank 1170 of
2106 — the bright burger's gloss and melt did not beat the ramen's
steamy, editorial depth. v3 changes the dish again, and this time it
leans into the strongest signals in the judge's own rubric: a dessert
built entirely around melt and gloss (criterion 2), plated with one
focal point under hard, dramatic light (criterion 3), its dark plate
and deep palette giving it the same chiaroscuro mood that made the
ramen work, while the ice cream, raspberries and salt keep it fresh
and real rather than a single brown mass.

## How the entry works

The picture is the entry and the code only delivers it. `main.py` is a
Python 3.13 program using nothing but the standard library. It finds
`food.jpg` next to itself, names its format from the leading bytes
(JPEG or PNG — anything else stops the program), then streams it chunk
by chunk to `entry.png` in the output directory, where the grader reads
it. After the copy it proves the handover landed whole: the destination
must be exactly the same size as the source, and its first bytes must
match the source's, or the program fails instead of handing over a
broken picture.

The output directory comes from the `MAKEFUN_OUTPUT_DIR` environment
variable, defaulting to `/output`. The destination is always called
`entry.png`, following the gate's convention, even though the bytes are
JPEG — the gate tells the formats apart from their leading bytes, and
both are accepted.

## Limits

- Image: 1024x1024 pixels, 217,288 bytes — inside the 1 MiB and
  1024x1024 limits.
- Program: Python 3.13, standard library only, no network.

## Running it

```sh
mkdir -p /tmp/out-food && MAKEFUN_OUTPUT_DIR=/tmp/out-food python3 main.py
```

After that, `/tmp/out-food/entry.png` exists and is an exact copy of
`food.jpg` — the same 217,288 bytes. The program prints the destination
path and byte count on success.
