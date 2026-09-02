# med-computation Operating Rules

## Project
Computational medicine study/code repo — simulations (SIR, agent-based models),
deep learning notes, R-based bioinformatics analysis (e.g. RNA-seq).

## Naming Convention
- Folder names: lowercase kebab-case (e.g. `agent-based-model`, `deep-learning-specialization`,
  `r-data-analysis`). Established 2026-09-01 while the repo was still small; keep new folders
  consistent with this.
- `test.py` is a scratch file, intentionally gitignored — do not track it.

## Working Style
- This is a study repo, not a product build — the user is learning by doing the work
  themselves, not delegating it. Established 2026-09-01 after re-implementing a paper's
  snMultiome pipeline (system installs, environment setup, data downloads).
- Default to explaining and guiding: give clear step-by-step manual instructions the user
  runs themselves (terminal commands, install steps, config edits) rather than executing
  multi-step setup/automation (installers, package installs, pipeline runs, data downloads)
  on their behalf.
- Exploration/research (reading code, fetching papers, web search, inspecting existing repo
  files) is fine to do directly — the line is at *doing the exercise for them*, not at
  reading and reporting back.
- If unsure whether a step is "explain" vs "do", ask, or default to explaining.

## Commit Workflow
- After a meaningful, commit-worthy unit of work is done (not every tiny edit), propose a commit:
  draft the commit message and show it to the user.
- Wait for the user's approval before actually running `git commit`. Do not commit silently.
- Do not push to origin unless the user separately asks.
