# core/config.py
import os

# =============================
# Project root (repo root)
# =============================
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# =============================
# Workspace / Examples (repo-relative)
# =============================
WORKSPACE_ROOT = os.path.join(PROJECT_ROOT, "workspace")
EXAMPLES_ROOT = os.path.join(PROJECT_ROOT, "examples")

# FileExplorer root (optional)
# - default: repo root
# - can override by env var (useful on server)
EXPLORER_ROOT = os.environ.get("EXPLORER_ROOT", PROJECT_ROOT)

# Inference results (runtime output; should be gitignored)
INF_RESULTS_ROOT = os.environ.get(
    "INF_RESULTS_ROOT",
    os.path.join(PROJECT_ROOT, "inf_results"),
)

# =============================
# Upload / runtime directories (repo-relative)
# =============================
# NOTE: keep variable names to minimize refactor in other modules
UPLOAD_ROOT = os.environ.get("UPLOAD_ROOT", WORKSPACE_ROOT)
UPLOAD_NEWDATASET_ROOT = os.environ.get(
    "UPLOAD_NEWDATASET_ROOT",
    os.path.join(WORKSPACE_ROOT, "datasets_for_labeling"),
)
UPLOAD_DATA_DIR = os.environ.get(
    "UPLOAD_DATA_DIR",
    os.path.join(WORKSPACE_ROOT, "configs"),
)
UPLOAD_MODEL_DIR = os.environ.get(
    "UPLOAD_MODEL_DIR",
    os.path.join(WORKSPACE_ROOT, "base_model"),
)

# Training runs directory (runtime output; should be gitignored)
RUNS_DIR = os.environ.get(
    "RUNS_DIR",
    os.path.join(PROJECT_ROOT, "runs"),
)

# Labeling destination root (runtime output; should be gitignored)
LABELING_DEST_ROOT = os.environ.get(
    "LABELING_DEST_ROOT",
    os.path.join(WORKSPACE_ROOT, "datasets_for_labeling"),
)

# =============================
# External commands (overrideable)
# =============================
# For GitHub/paper: default to generic commands
# For your server: set env vars to point to venv binaries if needed
TRAIN_ENV_PY = os.environ.get("TRAIN_ENV_PY", "python")
YOLO_CLI = os.environ.get("YOLO_CLI", "yolo")

# =============================
# Metrics / Loss columns (keep as-is)
# =============================
METRIC_COLUMNS = [
    "metrics/mAP50-95(B)", "metrics/mAP50(B)",
    "metrics/precision(B)", "metrics/recall(B)",
    "metrics/mAP50-95(M)", "metrics/mAP50(M)",
    "metrics/precision(M)", "metrics/recall(M)",
]

LOSS_COLUMNS = [
    "train/box_loss", "train/seg_loss", "train/cls_loss", "train/dfl_loss",
    "val/box_loss", "val/seg_loss", "val/cls_loss", "val/dfl_loss",
]

