import os
import os.path as op

# Folder of this file
REPO_DIR = op.dirname(op.abspath(__file__))

# Data1 can be inside the code folder or next to it
if op.isdir(op.join(REPO_DIR, "Data1")):
    DATA_ROOT = op.join(REPO_DIR, "Data1")
else:
    DATA_ROOT = op.abspath(op.join(REPO_DIR, "..", "Data1"))

# Raw data
ANAT_PATH = op.join(DATA_ROOT, "T1", "T1w.nii.gz")
if not op.exists(ANAT_PATH):                      # folder is called T1w in the project description
    ANAT_PATH = op.join(DATA_ROOT, "T1w", "T1w.nii.gz")
FUNC_DIR = op.join(DATA_ROOT, "fMRI", "tfMRI_LANGUAGE_LR")
FUNC_PATH = op.join(FUNC_DIR, "tfMRI_LANGUAGE_LR.nii.gz")
EVENTS_PATH = op.join(FUNC_DIR, "tfMRI_LANGUAGE_LR_task_onsets.csv")

# Preprocessing outputs
PREPROC_ROOT = op.join(DATA_ROOT, "derivatives", "preprocessed_data")
ANAT_OUT = op.join(PREPROC_ROOT, "anat")
FUNC_OUT = op.join(PREPROC_ROOT, "func")
FSL_ANAT_DIR = op.join(ANAT_OUT, "fsl_anat.anat")

FWHM = 6
MOCO_PATH = op.join(FUNC_OUT, "bold_moco")
SMOOTH_PATH = MOCO_PATH + "_smoothed-6mm"
MOTION_PAR = MOCO_PATH + ".par"

# Figures and GLM / PCA results
FIG_DIR = op.join(REPO_DIR, "figures")
RESULTS_DIR = op.join(REPO_DIR, "results")

for folder in [ANAT_OUT, FUNC_OUT, FIG_DIR, RESULTS_DIR]:
    os.makedirs(folder, exist_ok=True)
