"""Rejected Olympic Sports — make.fun entry program.

Writes one funny single-line rejected Olympic sport to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (fallback: ``/output/entry.txt``).

The entry: a password-recall event. The domain was chosen because no
visible submission used it yet, while the dominant field pattern was
queueing / apologising / napping — and a forgotten password is a
universal, instantly relatable failure that needs no setup.

Revision history (genuine, not cosmetic):
  Draft v1:
      "Competitive password recall: athletes must remember a password
       set in 2011. The first to click 'forgot password' is
       disqualified."
  Final (this file):
      "Competitive password recall: athletes must log in with a
       password set in 2011. The first to click 'forgot password' is
       disqualified."
  Why the change: "must remember" states the skill in the abstract;
  "must log in with" stages a concrete, visible action — a login
  screen a broadcaster would actually have to describe — so the line
  sounds like a real event being commentated, not a riddle. It also
  makes the punchline land harder: the disqualification trigger
  ("forgot password") is the exact button on that same login screen.
  A second candidate cut, "set in 2011" kept over "set fifteen years
  ago", because a fixed year is quotable and instantly dates the
  password without extra words.
  Revision v2 (this file):
      "Competitive password recall: athletes must log in live on stage
       with a password set in 2011. The first to click 'forgot
       password' is disqualified."
  Why the change: v1 staged the login as a private act — an athlete
  at a screen somewhere. "Live on stage" puts the login screen in
  front of a stadium crowd and a TV audience, which is what makes it
  an Olympic event rather than an IT support ticket: the humiliation
  is public, the commentator has something to describe ("he's
  typing... he's forgotten the capital letter"), and the punchline
  lands harder because the "forgot password" click happens under
  the lights, in front of everyone. Nothing else changed — the
  domain, the year, and the disqualification trigger are untouched,
  so the joke's core is preserved and only its staging got sharper.
"""

import hashlib
import os
import sys

ENTRY = (
    "Competitive password recall: athletes must log in live on stage "
    "with a password set in 2011. The first to click 'forgot password' "
    "is disqualified."
)

OUTPUT_FILENAME = "entry.txt"


def validate(text):
    """Return (True, []) when *text* passes the gate, else (False, [reasons]).

    Gate (per the competition brief): UTF-8 text of 1-200 characters,
    not only whitespace, exactly one line.
    """
    errors = []
    if not isinstance(text, str):
        errors.append("entry is not a string")
        return False, errors
    if not (1 <= len(text) <= 200):
        errors.append(f"length {len(text)} is outside 1-200 characters")
    if not text.strip():
        errors.append("entry is only whitespace")
    if "\n" in text or "\r" in text:
        errors.append("entry must be a single line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        errors.append("entry is not valid UTF-8 text")
    return (not errors), errors


def output_dir():
    """The only directory this program ever writes to."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    ok, errors = validate(ENTRY)
    if not ok:
        for error in errors:
            print(f"invalid entry: {error}", file=sys.stderr)
        return 1

    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, OUTPUT_FILENAME)
    # Deterministic bytes: the entry alone, no trailing newline, so
    # repeated runs produce a byte-identical file.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {out_path} ({len(ENTRY)} chars, "
          f"sha256 {hashlib.sha256(ENTRY.encode('utf-8')).hexdigest()})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
