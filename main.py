"""Write the relaxing entry text to the output directory.

The grader runs this program and reads /output/entry.txt
(MAKEFUN_OUTPUT_DIR stands in for /output outside the grader).
Python 3.13 standard library only; no network; deterministic.
"""

import os

TEXT = (
    "Evening light rests on the river, and the river carries it "
    "without hurrying. A heron stands in the shallows, "
    "still as stone. Upstream, rain is falling on "
    "leaves, and the water keeps its slow promise: everything "
    "arrives, and nothing is chased."
)


def main():
    # The entry must be 1-280 Unicode code points, not only whitespace.
    assert 1 <= len(TEXT) <= 280, len(TEXT)
    assert TEXT.strip(), "entry text must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
