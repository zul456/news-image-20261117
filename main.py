#!/usr/bin/env python3
"""news-image-20261117 entry: copy the pre-rendered entry.png to the output.

The image (a 1024x1024 front page summing up Tuesday 17 November 2026
world news) is built at authoring time and shipped in this repository as
entry.png. This program only copies it to the grader's output directory,
so both runs write byte-identical output. Standard library only.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUTDIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUTDIR, "entry.png")

os.makedirs(OUTDIR, exist_ok=True)
shutil.copyfile(SRC, DST)
# The gate reads the whole file: fail loudly if the copy is short.
if os.path.getsize(DST) != os.path.getsize(SRC):
    raise RuntimeError("entry.png copy incomplete")
