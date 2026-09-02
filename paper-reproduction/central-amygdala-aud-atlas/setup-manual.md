# Setup Manual: Central Amygdala AUD snMultiome Atlas


## Paper Information

- Title: Central amygdala single-nucleus atlas reveals chromatin and gene transcription dynamics in human alcohol use disorder
- DOI: https://doi.org/10.1038/s41467-026-68351-1
- Preprint (if any):


## Method Analysis

- **Assay type:** 10x Chromium Single Cell Multiome.
- **Platform**: Paired-end 150bp reads, Illumina NovaSeq 6000, sequencing depth up to 500 million read pairs per sample.
- **Sample size / structure**: 50 postmortem donors — 22 with AUD (9 female, 13 male), 28 controls (17 female, 11 male). Central amygdala tissue. After QC: 174,188 high-quality nuclei (~6,028 reads/nucleus average).
- **Named software/pipeline**: CellRanger ARC v2.0.2 → ArchR v1.0.3 (ATAC) + Signac/Seurat (RNA) → Pegasus v1.5.0 → chromVAR, MAST/Wilcoxon DE, pseudobulk DESeq2, SuSiE fine-mapping, LDSC.


## Data  & Code Availability

- snMultiome data: Available from the corresponding author
    - Zenodo database [10.5281/zenodo.17656668]
    - Requests: https://www.research.va.gov/programs/tissue_banking/ptsd/
    - And/or email the corresponding author directly.
- Processed data: Freely available
    - https://www.nature.com/articles/s41467-026-68351-1#Sec31
    - [10.5281/zenodo.17656668](https://zenodo.org/records/17656668)
   - `AUDsnCEA-main.zip` — the analysis code (already cloned locally, see below)
   - `CNA-RNA.h5ad` (2.0 GB) — processed snRNA-seq (Pegasus/AnnData format)
   - `snATAC-seq.zip` (1.8 GB) — processed snATAC-seq (ArchR project)
- Code availability: Freely available
    - https://github.com/mjgirgenti/AUDsnCEA


## Repository Cloning

- Verifying it's the right repo:
    - Figure match: yes
    - no tag, no release
    - Last commit: Jul 11, 2025
    - Publication: Jan 19, 2026
- License: No license file in the repo
- Repo size: 20817 kb
- Direct clone or Shallow clone: Direct


## Environment Setting (paper's own)

- Software/OS compatibility: ArchR — Linux/macOS only
- System: r-base, build-essential, libcurl4-openssl-dev, libssl-dev, libxml2-dev, libhdf5-dev, libgsl-dev, git
- R:
    - BiocManager
    - ArchR (v1.0.3)
    - ArchR::installExtraPackages() (MACS2, genome annotations)
    - Signac (v1.11.0)
    - Seurat
    - GenomicRanges
    - rhdf5
- Python:
    - pegasuspy (v1.5.0)
    - scanpy
    - anndata


## Environment Setting (me)

- System (WSL2 Ubuntu, via apt): r-base, build-essential, libcurl4-openssl-dev, libssl-dev, libxml2-dev, libhdf5-dev, libgsl-dev, git
- R in WSL2 (renv, project-scoped):
    - BiocManager
    - ArchR
    - ArchR::installExtraPackages() (MACS2, genome annotations)
    - Signac
    - Seurat
    - GenomicRanges
    - rhdf5
- Python in WSL2 (conda env: 'aud-cea'):
    - pegasuspy
    - scanpy
    - anndata


## Paper's own code

| Folder | Content |
|---|---|
| `fig1-UMAP/` | Cell-type taxonomy UMAPs (RNA/ATAC/combined) + marker gene tracks. Has `analysis_R.ipynb`, `analysis_Py.ipynb`, `figures_R.ipynb`, `figures_Py.ipynb` |
| `fig2-Atlas/` | Inhibitory neuron subtypes, oligodendrocyte/immune classification. **Python only** |
| `fig3-DEG/` | AUD vs control differential expression. **Python only** |
| `fig4-P2G/` | Cis-regulatory elements, peak-to-gene links. R + Py |
| `fig5-GRN/` | KLF transcription factor regulatory networks. R + Py |
| `fig6-GWAS/` | GWAS fine-mapping. R + Py |
| `ED_fig*/` | Extended data figures (DEG GO enrichment, DEG subtypes, DEG GWAS, P2G, GRN, mouse validation) |
| `scATAC/script_0..8*.r` | The raw-to-processed ATAC pipeline: `script_0` starts from CellRanger ARC's `filtered_feature_bc_matrix.h5` output via `import10xFeatureMatrix()`, through tiling, doublet filtering, peak/motif calling (this is what produced the ArchR project bundled in `snATAC-seq.zip`) |
| `scRNA/` | `DEG_MAST.R` and Pegasus-based Wilcoxon DE notebook |