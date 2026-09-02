# Reproducing a Published Sequencing Study From Raw Data — General Manual

A reusable checklist for the situation "I have a paper with a graph I want to
regenerate myself, starting from (or as close as possible to) raw sequencing
data." Written after working through this once end-to-end; see
`central-amygdala-aud-atlas/setup-manual.md` for a worked example.

## 1. Read the Methods section first, not the figure

Before touching data, find out from the Methods:
- **Assay type**: bulk RNA-seq, scRNA-seq, snRNA-seq, ATAC-seq, multiome
  (RNA+ATAC), WGS/WES, etc.
- **Platform**: Illumina model, read length, paired vs single-end, kit
  (e.g. 10x Chromium, Smart-seq).
- **Sample size / structure**: number of donors/replicates, conditions —
  this tells you how big a download you're actually signing up for.
- **Named software/pipeline**: aligner, quantifier, package names and
  versions (e.g. CellRanger, STAR, ArchR, Seurat, DESeq2). Write these down —
  you'll need matching or compatible versions later.

## 2. Find the Data Availability Statement

This is usually a short paragraph near the end of the paper (or in a
"Data Availability" section separate from Methods). Look for:

- **Public accession numbers**: GEO (`GSExxxxx`), SRA (`SRPxxxxx`/`PRJNAxxxxx`),
  ENA, ArrayExpress, Zenodo, EGA. These mean you can download directly, no
  request needed.
- **Controlled-access accessions**: dbGaP (`phsxxxxxx`), EGA studies requiring
  a Data Access Committee, or informal "available upon request" language
  (often for human subject data with consent restrictions). These require:
  - A formal request, often through the hosting institution or a named
    program (e.g. a VA tissue bank, a specific brain bank).
  - Possibly your own institution's IRB approval and a signed Data Use
    Agreement.
  - Real wait time — days to weeks, not instant.
- **Split availability** is common: *processed* data (count matrices, final
  objects) publicly deposited, while *raw* reads (FASTQs) are controlled
  access or require a separate manual request. Don't assume "data available"
  means raw reads are available — check which tier each accession covers.

If accession numbers aren't in the statement, search `"<paper title>" GEO`
or `"<paper title>" dbGaP` — sometimes they're only in supplementary tables.

## 3. Find a companion code repository

Check for a GitHub/GitLab link in the Data/Code Availability statement,
supplementary methods, or search `<lead author or lab name> github <topic>`.
If one exists:

- Skim the directory structure for a figure-to-script mapping (papers with
  many figures often organize code as `fig1/`, `fig2/`, etc. — huge time
  saver if so).
- Check the README for setup instructions — often minimal or absent; don't
  expect much.
- **Expect hardcoded absolute paths** to the authors' own HPC/cluster
  filesystem. You will need to edit these to point at your local data
  location before anything runs.
- Note the exact package versions imported (e.g. `library(ArchR)` — check
  their `sessionInfo()` if included, or a `renv.lock`/`requirements.txt`).

## 4. Check software/OS compatibility BEFORE installing anything

Bioinformatics tools frequently have platform restrictions (many
Linux/macOS-only, especially anything wrapping samtools/bedtools/HDF5 C
libraries). Do this right after cloning the code repo, before running any
install command.

**Step 1 — get the full dependency list in one shot**, instead of reading
every notebook line by line:
```bash
grep -rh "^library(" paper-code/ | sort -u        # R
grep -rhE "^(import|from) " paper-code/ | sort -u  # Python
```

**Step 2 — for each package, check its own docs/CRAN page/GitHub README**
for an OS support note. Most bioinformatics tools state it explicitly
("Linux/macOS only," "not tested on Windows") right in their README or
install instructions.

**Step 3 — one blocker decides the whole environment.** You don't need
every package to be incompatible — just one that's tightly coupled into the
same scripts as everything else (e.g. ArchR forcing the entire R side onto
WSL even though Signac/Seurat alone would run fine on native Windows).

For each major tool named in Methods, check:

- Does it support your OS natively?
- If not: WSL2 (Windows), Docker/Singularity container, or a remote/cloud
  Linux environment are the usual fallbacks.
- Decide this **before** downloading multi-GB data — no point pulling data
  you can't yet process.

## 5. Set up an isolated, version-pinned environment

- R: `renv` (or at minimum match Bioconductor/CRAN package versions cited).
- Python: `conda`/`mamba` or `venv` + `requirements.txt`, matching cited
  versions where given.
- Version drift between what the paper used and what installs today is a
  common source of subtly different results (or outright breakage) —
  pin versions where the paper specifies them.

## 6. Validate against processed data before attempting raw reprocessing

Cheapest sanity check, in order:

1. Download the authors' **processed** data/objects first (usually much
   smaller than raw reads).
2. Get their own plotting/figure code running against that processed data.
   This confirms your environment is correctly set up without yet touching
   the expensive raw-data reprocessing step.
3. Only once that works, attempt to regenerate the processed data yourself
   from raw reads (alignment/quantification), and compare your output
   against the authors' deposited processed objects as ground truth.

## 7. Expect friction, budget for it

- Hardcoded paths and undocumented environment assumptions in the authors'
  code are the norm, not the exception.
- Raw controlled-access data may take weeks to arrive, or may never be
  granted — plan your near-term work around the processed/public tier and
  treat raw reprocessing as a stretch goal, not the starting point.
- Compute cost: raw alignment of deep sequencing (hundreds of millions of
  read pairs per sample, tens of samples) is a real time/disk/compute
  commitment — know what you're signing up for from the sample size you
  noted in step 1.
