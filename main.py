"""One Line, One Laugh — write the single funny line to /output/entry.txt.
Standard library only, no network, deterministic."""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

ENTRY = "I told my Wi-Fi we\u2019re growing apart \u2014 now it only connects when it feels like it.\n"

os.makedirs(OUT, exist_ok=True)
# The gate allows 1 to 140 characters: fail loudly rather than hand in an
# invalid entry.
if not 1 <= len(ENTRY) <= 140:
    raise SystemExit("entry.txt length out of gate: %d chars" % len(ENTRY))
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as fh:
    fh.write(ENTRY)
