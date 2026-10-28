"""
Shared paths for the whole project. Every notebook does `from paths import *`,
so a path only ever needs to be fixed here.

Data1 can sit either INSIDE the repo (Project1_NSSP/Data1) or NEXT TO it
(myfiles/Data1): both work. Data1/ is in .gitignore, so it is never pushed.
"""
import os
import os.path as op

REPO_DIR = op.dirname(op.abspath(__file__))

_candidates = [op.join(REPO_DIR, "Data1"), op.join(REPO_DIR, "..", "Data1")]
DATA_ROOT = next((op.abspath(p) for p in _candidates if op.isdir(p)), None)
if DATA_ROOT is None:
    raise FileNotFoundError(f"Data1 not found. Looked in: {[op.abspath(p) for p in _candidates]}")

# The T1 folder is called "T1" in our download ("T1w" in the project PDF): accept both
_t1 = [op.join(DATA_ROOT, d, "T1w.nii.gz") for d in ("T1", "T1w")]
ANAT_PATH = next((p for p in _t1 if op.exists(p)), _t1[0])

FUNC_DIR = op.join(DATA_ROOT, "fMRI", "tfMRI_LANGUAGE_LR")
FUNC_PATH = op.join(FUNC_DIR, "tfMRI_LANGUAGE_LR.nii.gz")
EVENTS_PATH = op.join(FUNC_DIR, "tfMRI_LANGUAGE_LR_task_onsets.csv")

# Everything we compute goes to Data1/derivatives (never inside the repo)
PREPROC_ROOT = op.join(DATA_ROOT, "derivatives", "preprocessed_data")
ANAT_OUT = op.join(PREPROC_ROOT, "anat")
FUNC_OUT = op.join(PREPROC_ROOT, "func")
FSL_ANAT_DIR = op.join(ANAT_OUT, "fsl_anat.anat")          # created by fsl_anat

FWHM = 6                                                    # smoothing kernel (mm)
MOCO_PATH = op.join(FUNC_OUT, "bold_moco")                  # FSL style: no extension
SMOOTH_PATH = MOCO_PATH + f"_smoothed-{FWHM}mm"
MOTION_PAR = MOCO_PATH + ".par"

# Figures and GLM maps stay in the repo folder but are git-ignored
FIG_DIR = op.join(REPO_DIR, "figures")
RESULTS_DIR = op.join(REPO_DIR, "results")

for _d in (PREPROC_ROOT, ANAT_OUT, FUNC_OUT, FIG_DIR, RESULTS_DIR):
    os.makedirs(_d, exist_ok=True)

if __name__ == "__main__":
    for k, v in sorted(globals().items()):
        if k.isupper():
            print(f"{k:13s} {v}   {'OK' if op.exists(str(v)) or not str(v).startswith('/') else 'MISSING'}")
