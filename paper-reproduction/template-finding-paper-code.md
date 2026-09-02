# Template: Finding and Cloning a Paper's Code Repository

General, reusable — not tied to any one project. Companion to
`reproducing-published-studies.md` step 3. Copy this file into a project's
notes and fill in the blanks for each paper you work through.

## Paper

- Title:
- Corresponding/lead author:
- DOI:
- Preprint (if any):

## Where I looked

*(check off / fill in as you go — hints under each)*

- [ ] Code Availability statement — found at:
      _(often separate from "Data Availability" — check both)_
- [ ] Supplementary Information / Methods PDF — found at:
      _(repo links sometimes only appear there, not the main text)_
- [ ] bioRxiv/medRxiv preprint version — found at:
      _(preprints often keep a repo link even when the published version's
      link rots or changes)_
- [ ] Journal's own code/software links widget — found at:
- [ ] Search `<lead author name> github <topic keywords>` — result:
- [ ] Search `<paper title> github` — result:
- [ ] Lab/senior-author GitHub organization — found at:
      _(first-author repos sometimes move under it later)_
- [ ] Papers With Code (paperswithcode.com) — result:
      _(if ML/computational-method adjacent)_
- [ ] Zenodo / Software Heritage (search title or DOI) — found at:
      _(authors sometimes archive a permanent snapshot here even when GitHub
      is the primary home)_

**Repo URL found:**

## Verifying it's the right repo

- Linked from the paper or supplement itself? (not just a plausible search
  hit):
- Tag/release matching the publication (e.g. `v1.0`, date-stamped tag)?
  _(pins you to what actually generated the figures, if code has moved on
  since)_:
- If no tag: last commit date vs. submission/publication date:
- Folder names vs. paper's figure numbers — do they line up (e.g. `fig1/`,
  `fig2/`)?

## Before cloning

- License:
- Repo size / large files committed directly? Shallow clone
  (`--depth 1`) needed?

## Clone command used

```bash
git clone <repo-url>
# or, pinned to a specific release:
git clone --branch v1.0 <repo-url>
```

*(Plain ZIP alternative: GitHub → green "Code" button → "Download ZIP" —
no git needed, but no easy pin/pull later.)*

## First look after cloning

- README summary / setup instructions given:
- Environment/dependency file found (`requirements.txt`, `environment.yml`,
  `renv.lock`, `DESCRIPTION`, `Dockerfile`, none):
- Hardcoded absolute paths found (examples) — will need retargeting:
- Execution order between scripts/notebooks (standalone vs. chained):

## If no repo exists at all

- Pseudocode / detailed-enough parameters in supplementary methods?
- Emailed corresponding author — date sent / response:
- Related paper from the same group with an overlapping-method repo?
