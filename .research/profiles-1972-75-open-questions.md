# Open identity questions from the 1972-75 profile pass, 24 August 2026

Two people in this batch are each carried in the record under two headwords in
adjacent years. Neither was merged, because merging asserts two names are one
human and that is an editor's call, not a research agent's. Both are recorded
here with the evidence so the decision can be made once.

## 1. Michael Inman / Mike Inman

`data/years.json` holds:

- 1972-73 senate member "Michael Inman", seat: sophomore class vice president
- 1973-74 senate member "Michael Inman", seat: junior class president
- 1974-75 senate member "Mike Inman", seat: senior class president

`data/name-aliases.json` has no entry, so the build writes two person pages and
a three-year Congress career reads as two people.

Evidence that they are one man, from WKU's own sources:

- The 1975 Talisman Who's Who entry (p. 95) lists his accomplishments as
  "president of his junior and senior classes, vice-president of his sophomore
  class" - the university's own source tying all three years to one person.
- The 1975 name index reads "Inman, Michael Thomas 95, 303, 314-315, 344, 361",
  a single index entry covering the Who's Who page, the Scabbard and Blade and
  Organizations pages, the senior class pages and the senior directory.
- The 1973 index reads "Inman, Michael Thomas, 210, 311, 344, 416" - the same
  full name, one entry.
- Both volumes' directories give Harrodsburg.

Recommended: add `"Mike Inman": "Michael Inman"` to name-aliases.json.

## 2. Carl Stolzfus / Carl Stoltzfus

`data/years.json` holds:

- 1972-73 senate member "Carl Stolzfus", seat: Academic Council representative,
  College of Education
- 1973-74 senate member "Carl Stoltzfus", seat: senior class president

Evidence, per the verifier's check of both yearbooks:

- Every appearance across the 1973 and 1974 Talisman gives **Stoltzfus** - the
  Sigma Phi Epsilon chapter pages, the Who's Who entry (1974, no. 16, p. 93),
  the senior class pages, the 1973 staff contributor list, and both name indexes
  ("Stoltzfus, Carl Leroy, 309, 413" in 1973; "Stoltzfus, Carl Leroy 93, 292,
  294, 380" in 1974).
- The Herald's index of his own letter of 4 December 1973 also gives Stoltzfus.
- The single **Stolzfus** is the Herald's index line for his letter of
  13 April 1973, and that is the spelling the 1972-73 Congress record was built
  on.

Recommended: keep the plate spelling visible, but fold the two under one person.
Per CLAUDE.md's "flag, do not fix" rule this is left for the editor rather than
changed here.

## 3. Not merged, deliberately

- **Deborah Locke.** The 1975 Talisman index carries "Brooks, Deborah J. Locke
  347" and a senior directory entry "DEBORAH LOCKE BROOKS". The verifier
  rejected treating this as her married name: nothing links that person to
  Deborah Jane Locke beyond a shared forename and initial, in a volume whose
  index carries several other Lockes (Debbie Ann Webb, Billie June, Phillip
  Marshall). She is also a one-term class officer with no later service, so a
  married name serves no counting purpose. The claim was cut from her profile.
- **Christy Kay Vogt.** The 1973-74 freshman class vice-president is recorded
  under that name string; the president of 1976-77 is recorded as "Christy
  Vogt", and her existing leader profile already states she "ran for and won
  freshman vice president" as a freshman. No alias entry exists, so the two
  name strings build two person pages. Flagged, not changed.
- **Jeff Wampler / Michael David Wampler.** Two different men in the 1976
  Talisman index ("Wampler, Jeffrey Lee 88, 322" and "Wampler, Michael David
  288"). A draft citation in this pass pointed at p. 288 and was corrected to
  322 before publication. They must not be folded together.
- **Debbie Filburn / Donna Filburn.** Sisters, both in the Associated Student
  Government, correctly held apart in the record already. The 1975 Talisman
  Kappa Delta page (p. 252) states it outright and each has her own index entry.
