# Project1_NSSP – NX-421 mini-project (HCP language task)

## Files
| File | What | Tasks |
|---|---|---|
| `paths.py` | All paths, in one place | – |
| `utils.py` | Lab helpers (FSL, FSLeyes) | – |
| `1_preprocessing.ipynb` | Structural + functional preprocessing | 1.1, 1.2 |
| `2_glm.ipynb` | Design matrix, GLM, contrasts, networks | 1.3 |
| `3_<pca/ica/kmeans>.ipynb` | Part 2 (to do) | Part 2 |

Run the notebooks **in this order**. The data must be in `Data1/` (inside this folder or next to it), with `Data1/T1/T1w.nii.gz` and `Data1/fMRI/tfMRI_LANGUAGE_LR/...`.

## Rules for the group
1. `git pull` **before** starting to work.
2. One person per notebook at a time (say it in the group chat) – notebooks can't be merged.
3. Before pushing: **Edit → Clear Outputs of All Cells**, save, then `git add` / `commit` / `push`.
4. Never push data, `.nii.gz`, `figures/` or `results/` (they are in `.gitignore`).
5. Python goes in notebooks, never in the terminal (typing `import ...` in a terminal creates huge screenshot files).
