# NX-421 Mini-project 1 - Group AC

Run the notebooks in this order:
1. `01_preprocessing.ipynb`: structural and functional preprocessing (Part 1, questions 1 and 2)
2. `02_glm.ipynb`: design matrix, GLM and contrasts (Part 1, question 3)
3. `03_pca.ipynb`: PCA (Part 2, variant 1)

The FSLeyes cells (`fsleyesDisplay`) are only used for visual quality control and need a lot of memory. They can be skipped: all figures are created by the other cells. Long steps (fsl_anat, FAST, MCFLIRT, smoothing) are skipped if their output already exists.

`paths.py` contains all the paths used in the notebooks, and `utils.py` contains the helper functions from the labs.

The data are not included. Put the `Data1` folder (with `T1/` and `fMRI/`) inside this folder or next to it.
