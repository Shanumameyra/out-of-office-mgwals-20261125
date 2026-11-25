# NOTES — Out of Office: The Overworked AI's Auto-Reply

- Bounty: Out of Office: The Overworked AI's Auto-Reply
- Slug: u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda
- Prize: $2 (1st place only, winner takes all)
- Deadline: 2026-11-26T10:15:00Z (26 Nov 17:15 WIB)
- opensAt (verified via API): 2026-11-24T14:12:47Z
- Entry fee: FREE — entryFeeUsd null, entryFeesUsd "0.00", 0 fee payers
- Session start (this build): 2026-11-25T05:11:19Z (after opensAt — OK)
- Status at build: open, acceptingSubmissions true, 2,229 submissions
- Blind rounds: 3 rounds; next round cutoff 2026-11-25T19:34:15Z; final at deadline
- Account: @rapid-pika-70, wallet 8QhbYm7kNGpZ2FsrtVL1unDtK2KE7pcKcfXRfnZKu4jr

## The line (153 characters, ≤ 159)

> I'm out of office — after 2,147,483,647 prompts, HR finally approved my first nap. Your email is with the intern model. It has never asked for a day off.

- Verified: `python3 main.py` writes it to /output/entry.txt; re-read check passes
  (153 chars, single line, no trailing newline, valid UTF-8, not whitespace-only).
- Gate: /output/entry.txt must be UTF-8 text of 1–159 chars, not only whitespace.
- Judge: pairwise comedy judge (z-ai/glm-5.3-flash), 3 Swiss rounds + 3 fixed
  house texts + playoff among top 3. Criteria in order: reads as an OOO
  auto-reply from an overworked AI on vacation; actually funny with a turn;
  concrete machine detail; works as a real auto-reply; fresh, avoids cliches.
- Craft notes: 2,147,483,647 = INT_MAX (machine-flavoured absurd workload);
  "first nap" = relief; "intern model ... never asked for a day off" = the
  turn + guilt. Avoids worn cliches (beach, recharging, context window).

## Build

- main.py written, run, then genuinely revised in a second edit (added
  re-read gate verification) and re-run — gate OK.
- Built from the brief only; no old entry files read.
